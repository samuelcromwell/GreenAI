from django.contrib import admin
from django import forms
from .models import Contact, TeamMember, Subscriber, FooterGallery, Blog, FAQ, Investor, Product, Review, Sustainability, CSR, Initiative, CaseStudy, Solution, Opportunity, Feedback, Knowledge, Whitepaper
from .forms import ContactForm
from tinymce.widgets import TinyMCE
from django.utils import timezone
from django.core.mail import send_mail

# Define the custom admin form
class ContactAdminForm(forms.ModelForm):
    reply_message = forms.CharField(widget=forms.Textarea, required=False, label="Reply Message")

    class Meta:
        model = Contact
        fields = '__all__'

# Customize the admin class for Contact
class ContactAdmin(admin.ModelAdmin):
    form = ContactAdminForm
    list_display = ('name', 'email', 'subject', 'replied', 'replied_at')
    readonly_fields = ('replied', 'replied_at')

    def save_model(self, request, obj, form, change):
        if form.cleaned_data.get('reply_message'):
            # Send the reply email
            send_mail(
                subject=f"Re: {obj.subject}",
                message=form.cleaned_data['reply_message'],
                from_email='your-email@example.com',  # Replace with your actual email
                recipient_list=[obj.email],
            )
            obj.replied = True
            obj.replied_at = timezone.now()
            obj.reply_message = form.cleaned_data['reply_message']
        super().save_model(request, obj, form, change)

# Register the Contact model with the customized admin class
admin.site.register(Contact, ContactAdmin)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'received_at')

admin.site.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')
    fields = ('name', 'role', 'image', 'facebook_url', 'twitter_url', 'linkedin_url')

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')

@admin.register(FooterGallery)
class FooterGalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')


class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Blog
        fields = "__all__"

class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm

admin.site.register(Blog, BlogAdmin)


class SustainabilityAdminForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Sustainability
        fields = "__all__"

class SustainabilityAdmin(admin.ModelAdmin):
    form = SustainabilityAdminForm

admin.site.register(Sustainability, SustainabilityAdmin)

class CaseStudyAdminForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = CaseStudy
        fields = "__all__"

class CaseStudyAdmin(admin.ModelAdmin):
    forms = CaseStudyAdminForm

admin.site.register(CaseStudy, CaseStudyAdmin)

class SolutionAdminForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Solution
        fields = "__all__"

class SolutionAdmin(admin.ModelAdmin):
    forms = CaseStudyAdminForm

admin.site.register(Solution, SolutionAdmin)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)
    search_fields = ('question', 'answer',)

@admin.register(Knowledge)
class KnowledgeAdmin(admin.ModelAdmin):
    list_display = ('statement',)
    search_fields =('statement', 'description',)

@admin.register(Investor)
class InvestorAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    fields = ('name', 'position', 'image', 'facebook_url', 'twitter_url', 'linkedin_url')

@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('name', 'current_price')
    fields = ('name', 'image', 'brief_description', 'detailed_description', 'initial_price', 'current_price', 'slug')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'rating', 'created_at', 'message')
    list_filter = ('rating', 'created_at')
    search_fields = ('name', 'email', 'message')

@admin.register(CSR)
class CSR(admin.ModelAdmin):
    list_display = ('name', 'number')
    fields = ('name', 'number')

@admin.register(Initiative)
class Initiative(admin.ModelAdmin):
    list_display = ('title', 'image')
    fields = ('title', 'image', 'content', 'slug')

@admin.register(Opportunity)
class Opportunity(admin.ModelAdmin):
    list_display = ('title', 'organizer', 'venue', 'date_posted')
    search_fields = ('title', 'organizer')
    list_filter = ('date_posted', 'venue')

class WhitepaperAdminForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Whitepaper
        fields = "__all__"

class WhitepaperAdmin(admin.ModelAdmin):
    form = WhitepaperAdminForm

admin.site.register(Whitepaper, WhitepaperAdmin)
