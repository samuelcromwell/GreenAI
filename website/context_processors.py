from .models import FooterGallery

def footer_gallery_images(request):
    return {
        'images': FooterGallery.objects.all()
    }
