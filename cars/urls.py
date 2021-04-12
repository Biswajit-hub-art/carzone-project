from django.urls import path
from cars import views
urlpatterns=[
    path('', views.cars, name='cars'),
    path('car_detail/<int:id>', views.car_detail, name='car_detail'),
    path('search/', views.search, name='search'),
]
