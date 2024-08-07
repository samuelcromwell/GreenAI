import requests # type: ignore
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ContactForm, SubscribeForm
from .models import TeamMember, FooterGallery, Subscriber, Blog, FAQ, Investor
from django.http import JsonResponse
from django.conf import settings
from django.views import View
from django.core.paginator import Paginator

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    context = {'blog': blog}
    return render(request, 'website/blog_detail.html', context)


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
    # Fetch the latest 3 blog posts
    blogs = Blog.objects.order_by('-time')[:3]

    return render(request, 'website/index.html', {'form': form, 'blogs': blogs})

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
    investors = Investor.objects.all()
    return render(request, 'website/partners.html', {'investors': investors})

def feedback(request):
    return render(request, 'website/feedback.html')

def blogs(request):
    blogs = Blog.objects.all().order_by("-time")
    paginator = Paginator(blogs, 6)  # Paginate by 6 blogs per page
    page = request.GET.get("page")
    blogs = paginator.get_page(page)
    context = {"blogs": blogs}
    return render(request, "website/blogs.html", context)


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

def whitepapers(request):
    return render(request, 'website/whitepapers.html')

def FAQs(request):
    faqs = FAQ.objects.all()
    return render(request, 'website/FAQs.html', {'faqs': faqs})

def casestudies(request):
    return render(request, 'website/casestudies.html')
