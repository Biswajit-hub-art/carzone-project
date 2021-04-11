from django.shortcuts import render
from .models import Car
from django.core.paginator import Paginator
# Create your views here.
def cars(request):
    cars_list= Car.objects.order_by('-created_date')

    page = request.GET.get('page')
    paginator=Paginator(cars_list,3)
    paged_cars=paginator.get_page(page)

    context={
        'car_active': "active",
        'cars_list':paged_cars,
    }
    return render(request, 'cars/cars.html', context)


def car_detail(request,id):
    detail= Car.objects.get(id=id)
    context={
        'detail':detail,
    }
    return render(request, 'cars/car_detail.html', context)
