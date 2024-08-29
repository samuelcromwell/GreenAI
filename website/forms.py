from django import forms
from .models import Contact, Subscriber, Review, Feedback

class ContactForm(forms.ModelForm):
    reply_message = forms.CharField(widget=forms.Textarea, required=False, label="Reply Message")

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message', 'reply_message']
        widgets = {
            'subject': forms.Select(choices=Contact.SUBJECT_CHOICES),
        }

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['first_name', 'last_name', 'occupation', 'message']
        
# Still doesnt work
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'rating', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name*', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email*', 'class': 'form-control'}),
            'rating': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)], attrs={'class': 'star-rating'}),
            'message': forms.Textarea(attrs={'placeholder': 'Message', 'class': 'form-control'}),
        }

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Your email to subscribe to our Newsletter'})
        }