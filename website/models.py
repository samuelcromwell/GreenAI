from django.db import models

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
    accepted_terms = models.BooleanField(default=False)

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
