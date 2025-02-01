from django.http import HttpResponse
from django.views.generic import TemplateView

# c1/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from ..forms import RegistrationForm


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('home') 
    else:
        form = RegistrationForm()
    return render(request, 'c1/register.html', {'form': form})




def home(request):
    return HttpResponse("Welcome to the home page")

class ShowPageView(TemplateView):
    template_name = 'c1/main.html'
    
    