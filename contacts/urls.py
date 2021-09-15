from django.urls import path
from contacts import views
urlpatterns=[
    path('inquiry/', views.inquiry, name='inquiry'),
]
