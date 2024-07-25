from django import forms
from .models import Contact, Subscriber

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'subject': forms.Select(choices=Contact.SUBJECT_CHOICES),
        }

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        