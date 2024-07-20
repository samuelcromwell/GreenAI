from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import TeamMember

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('index')
        else:
            messages.error(request, 'There was an error in your form submission.')
    else:
        form = ContactForm()
    return render(request, 'website/index.html', {'form': form})



def about(request):
    team_members = TeamMember.objects.all()
    return render(request, "website/about.html", {'team_members': team_members})

def contact(request):
    return render(request, "website/contact.html")
