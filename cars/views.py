from django.shortcuts import render
from .models import Car
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.
def cars(request):
    cars_list= Car.objects.order_by('-created_date')
    page = request.GET.get('page')
    paginator=Paginator(cars_list,3)
    paged_cars=paginator.get_page(page)

    #search list naming.
    model_search=Car.objects.values_list('model', flat=True).distinct()
    city_search=Car.objects.values_list('city', flat=True).distinct()
    year_search=Car.objects.values_list('year', flat=True).distinct()
    body_style_search=Car.objects.values_list('body_style', flat=True).distinct()


    context={
        'car_active': "active",
        'cars_list':paged_cars,

        'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
    }
    return render(request, 'cars/cars.html', context)


def car_detail(request,id):
    detail= Car.objects.get(id=id)
    context={
        'detail':detail,
    }
    return render(request, 'cars/car_detail.html', context)

def search(request):
    cars= Car.objects.order_by('-created_date')

    #search list naming
    model_search=Car.objects.values_list('model', flat=True).distinct()
    city_search=Car.objects.values_list('city', flat=True).distinct()
    year_search=Car.objects.values_list('year', flat=True).distinct()
    body_style_search=Car.objects.values_list('body_style', flat=True).distinct()
    transmission_search=Car.objects.values_list('transmission', flat=True).distinct()

    keyword=request.GET.get('keyword')
    if keyword:
        cars=cars.filter(Q(description__icontains=keyword))

    model=request.GET.get('model')
    if model:
        cars=cars.filter(Q(model__icontains=model))

    city=request.GET.get('city')
    if city:
        cars=cars.filter(Q(city__icontains=city))

    year=request.GET.get('year')
    if year:
        cars=cars.filter(Q(year__icontains=year))

    body_style=request.GET.get('body_style')
    if body_style:
        cars=cars.filter(Q(body_style__icontains=body_style))

    transmission=request.GET.get('transmission')
    if transmission:
        cars=cars.filter(Q(transmission__icontains=transmission))


    min_price=request.GET.get('min_price')
    max_price=request.GET.get('max_price')
    if min_price and max_price:
        cars=cars.filter(Q(price__gte=min_price), Q(price__lte=max_price))

    context={
        'cars':cars,

        #search naming list
        'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
        'transmission_search':transmission_search,


    }
    return render(request, 'cars/search.html', context)
