from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

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

    if request.method=='POST':
        name = request.POST['name']
        email =  request.POST['email']
        subject =  request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        mail_subject = 'You have a message regarding the wheeler website '+ subject
        message_body = 'Name:' + name + ', email:' + email + ', Phone:' +phone

        admin_info = User.objects.get(is_superuser=True)
        admin_email=admin_info.email

        send_mail(
                mail_subject,
                message_body,
                'sahoob193@gmail.com',
                [admin_email],
                fail_silently=False,
                )

        messages.success(request, 'ThankYou for contacting us!')
        return redirect('contact')

    return render(request, 'pages/contact.html', context)
