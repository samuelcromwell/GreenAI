import requests # type: ignore
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm, SubscribeForm
from .models import TeamMember, FooterGallery, Subscriber, Blog
from django.http import JsonResponse
from django.conf import settings
from django.views import View
from django.core.paginator import Paginator


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'}, status=200)
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors.as_json()}, status=400)
    else:
        form = ContactForm()
    return render(request, 'website/index.html', {'form': form})

def about(request):
    team_members = TeamMember.objects.all()
    return render(request, 'website/about.html', {'team_members': team_members})
    
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'}, status=200)
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors.as_json()}, status=400)
    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})

def products(request):
    return render(request, 'website/products.html')

def solutions(request):
    return render(request, 'website/solutions.html')

def sustainability(request):
    return render(request, 'website/sustainability.html')

def support(request):
    return render(request, 'website/support.html')

def partners(request):
    return render(request, 'website/partners.html')

def feedback(request):
    return render(request, 'website/feedback.html')

def blog(request):
    blogs = Blog.objects.all().order_by("-time")
    paginator = Paginator(blogs, 3)
    page = request.GET.get("page")
    blogs = paginator.get_page(page)
    context = {"blogs": blogs}
    return render(request, "website/blog.html", context)

def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        email = request.POST.get('email')
        if Subscriber.objects.filter(email=email).exists():
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'message': 'You have already subscribed to our Newsletter'})
            else:
                messages.error(request, 'You have already subscribed to our Newsletter')
        elif form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'You have successfully subscribed to our Newsletter'})
            else:
                messages.success(request, 'You have successfully subscribed to our Newsletter')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'message': 'Subscription failed. Please enter a valid email address'})
            else:
                messages.error(request, 'Subscription failed. Please enter a valid email address')

    # For non-AJAX requests, redirect back to the referring page
    return redirect(request.META.get('HTTP_REFERER', 'home'))

def footer_gallery_view(request):
    images = FooterGallery.objects.all()
    return render(request, 'website/shared/footer.html', {'images': images})
