from django.shortcuts import render
from .models import Team
from cars.models import Car

# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars= Car.objects.order_by('-created_date').filter(is_featured=True)
    latest_cars=Car.objects.order_by('-created_date')

    context = {
        'teams' : teams,
        'home_active': "active",
        'featured_cars': featured_cars,
        'latest_cars':latest_cars,
    }
    return render(request, 'pages/home.html', context)

def about(request):
    teams = Team.objects.all()
    context={
        'teams' : teams,
        'about_active':"active",
    }
    return render(request, 'pages/about.html', context)

def services(request):
    context={
        'services_active':"active",
    }
    return render(request, 'pages/services.html', context)

def contact(request):
    context={
        'contact_active':"active",
    }
    return render(request, 'pages/contact.html', context)
