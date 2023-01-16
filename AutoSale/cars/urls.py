from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cars_home, name='cars_home'),
    path('add_car', views.add_new_car, name='add_new_car')
]
