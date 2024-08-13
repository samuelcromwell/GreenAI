from .models import FooterGallery
from .forms import SubscribeForm

def footer_gallery_images(request):
    return {
        'images': FooterGallery.objects.all()
    }

def subscribe_form(request):
    return {'subscribe_form': SubscribeForm()}