from django.db import models
from django.utils.text import slugify

class Contact(models.Model):
    SUBJECT_CHOICES = [
        ('fibre', 'Fibre Cables'),
        ('triple play','Triple Play 3-in-1 LED Lights'),
        ('installation','Installation Services'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100, choices=SUBJECT_CHOICES)
    message = models.TextField()

    def __str__(self):
        return self.name

class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    image = models.ImageField(upload_to='team/')
    
    def __str__(self):
        return self.name

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class FooterGallery(models.Model):
    image = models.ImageField(upload_to='footer_gallery/')

    def __str__(self):
        return self.image.name


class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    thumbnail_img = models.ImageField(null=True, blank=True, upload_to="blog_images/")
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    time = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

