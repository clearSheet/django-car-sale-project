from django.shortcuts import render
from .models import Card_Cars
from .  func import get_good_price


def cars_home(request):
    cars = Card_Cars.objects.all()
    for car in cars:
        car.price = get_good_price(car.price) + ' ₽'
    return render(request, 'cars/cars_home.html', {'cars': cars})

    # cars = Card_Cars.objects.order_by('price') # Сортировка по цене
    # cars = Card_Cars.objects.order_by('-price') # Сортировка по цене в обратной сторонге
    # cars = Card_Cars.objects.order_by('price')[:1] # Сортировка по цене и выбрать одну запись


def add_new_car(request):
    return render(request, 'cars/add_new_car.html')