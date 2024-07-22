from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import TeamMember

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully! We will respond soon')
            return redirect('index')
        else:
            messages.error(request, 'There was an error in your form submission. Kindly try again')
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
            messages.success(request, 'Your message has been sent successfully! We will get back to you soon')
            return redirect('contact')
        else:
            messages.error(request, 'There was an error in your form submission. Kindly try again')
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