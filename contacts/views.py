from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User


# Create your views here.
def inquiry(request):
    if request.method=="POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        customer_need=request.POST["customer_need"]
        car_title=request.POST["car_title"]
        city=request.POST["city"]
        state=request.POST["state"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        car_id=request.POST["car_id"]
        user_id=request.POST["user_id"]
        message=request.POST["message"]

        if request.user.is_authenticated:
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made a request wait until we get back to you!')
                return redirect('/cars/car_detail/'+car_id)

        contact=Contact(first_name=first_name, last_name=last_name, customer_need=customer_need,
        car_title=car_title, city=city, state=state, email=email, phone=phone, car_id=car_id,
        user_id=user_id, message=message)

        admin_info = User.objects.get(is_superuser = True)
        admin_email= admin_info.email
        send_mail(
                'New Car Inquiry',
                'You have a new Inquiry for the car' + car_title + '. Please login to your admin panel for more info.',
                'sahoob193@gmail.com',
                [admin_email],
                fail_silently=False,
                )

        contact.save()
        messages.success(request, 'Your request has been sent!')

        return redirect('/cars/car_detail/'+car_id)
