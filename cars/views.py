from django.shortcuts import render

# Create your views here.
def cars(request):
    context={
        'car_active': "active",
    }
    return render(request, 'cars/cars.html', context)
