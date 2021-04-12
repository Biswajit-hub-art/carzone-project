from django.shortcuts import render
from .models import Team
from cars.models import Car

# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars= Car.objects.order_by('-created_date').filter(is_featured=True)
    latest_cars=Car.objects.order_by('-created_date')
    # car_filter_field=Car.objects.values('model', 'city', 'year', 'body_style')
    model_search=Car.objects.values_list('model', flat=True).distinct()
    city_search=Car.objects.values_list('city', flat=True).distinct()
    year_search=Car.objects.values_list('year', flat=True).distinct()
    body_style_search=Car.objects.values_list('body_style', flat=True).distinct()

    context = {
        'teams' : teams,
        'home_active': "active",
        'featured_cars': featured_cars,
        'latest_cars':latest_cars,
        # 'car_filter_field':car_filter_field,
        'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
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
