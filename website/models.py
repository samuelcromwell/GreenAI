from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField
# from ckeditor.fields import RichTextField
from django.utils import timezone
from django.core.mail import send_mail

class Contact(models.Model):
    SUBJECT_CHOICES = [
        ('fibre', 'Fibre Cables'),
        ('triple play', 'Triple Play 3-in-1 LED Lights'),
        ('installation', 'Installation Services'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100, choices=SUBJECT_CHOICES)
    message = models.TextField()
    replied = models.BooleanField(default=False)
    reply_message = models.TextField(blank=True, null=True)
    replied_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Feedback(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    message = models.TextField()
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    image = models.ImageField(upload_to='team/')
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    
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
    title = models.CharField(max_length=55)
    content = HTMLField()
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
    
class Sustainability(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = HTMLField()
    thumbnail_img = models.ImageField(null=True, blank=True, upload_to="sustainability_images/")
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    time = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('sustainability_detail', kwargs={'slug': self.slug})    

    def __str__(self):
        return self.title

class CaseStudy(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=55)
    content = HTMLField()
    thumbnail_img = models.ImageField(null=True, blank=True, upload_to="case_studies/")
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    time = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('casestudies', kwargs={'slug': self.slug})
    
    def __str__(self):
        return self.title

class Whitepaper(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = HTMLField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('whitepaper_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
    
class CSR(models.Model):
    name = models.CharField(max_length=100)
    number = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return self.name
    
class Initiative(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='green_initiatives/')
    content = HTMLField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('initiative_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

class Solution(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='industry_solutions/')
    content = HTMLField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('industry_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    initial_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    brief_description = models.TextField(max_length=70)
    detailed_description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)
    time = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('product_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question

class Knowledge(models.Model):
    statement = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.statement
    
class Investor(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='investors/', blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.rating} Stars)"
    
class Opportunity(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField(max_length=250)
    image = models.ImageField(null=True, blank=True, upload_to="opportunity_images/")
    venue = models.CharField(max_length=255)
    organizer = models.CharField(max_length=100, default="GreenAI")
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title