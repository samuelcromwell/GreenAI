from django.contrib import admin
from django import forms
from .models import Contact, TeamMember, Subscriber, FooterGallery, Blog, FAQ

admin.site.register(Contact)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')

@admin.register(FooterGallery)
class FooterGalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')


class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'id': "richtext_field"}))

    class Meta:
        model = Blog
        fields = "__all__"

class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm

admin.site.register(Blog, BlogAdmin)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)
