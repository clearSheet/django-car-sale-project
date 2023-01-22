from django.db import models

# Create your models here.


class Card_Cars(models.Model):
    id = models.IntegerField('ID объявления', primary_key=True, auto_created=True)
    user_id = models.IntegerField('ID пользователя')

    brand = models.CharField('Марка автомобиля', max_length=250)
    model = models.CharField('Модель автомобиля', max_length=250)
    price = models.IntegerField('Цена автомобиля')
    about = models.TextField('Описание автомобиля')
    city_sale = models.CharField('Населенный пункт продажи', max_length=250)
    date = models.DateTimeField('Дата и время публикации', max_length=250)

    color = models.CharField('Цвет автомобиля', max_length=250)
    engine = models.CharField('Название двигателя', max_length=250)
    power = models.IntegerField('Мощность автомобиля')
    car_number = models.CharField('Номер автомобиля', max_length=250)
    vin_number = models.CharField('Вин номер автомобиля', max_length=250)
    millage = models.IntegerField('Пробег автомобиля')
    transmission = models.CharField('Привод автомобиля', max_length=250)

    def __str__(self):
        return self.brand + ' ' + self.model + ' (' + self.car_number + ')'

    class Meta:
        verbose_name = 'Карточка автомобиля'
        verbose_name_plural = 'Карточки автомобилей'


class Model_and_Brand_Cars(models.Model):
    id = models.IntegerField('ID', primary_key=True, auto_created=True)

    model = models.CharField('Модель автомобиля', max_length=250)
    brand = models.CharField('Марка автомобиля', max_length=250)

    def __str__(self):
        return self.brand + ' ' + self.model

    class Meta:
        verbose_name = 'Марка и модель автомобиля'
        verbose_name_plural = 'Марки и модели автомобилей'


class Brands_Cars(models.Model):
    id = models.IntegerField('ID', primary_key=True, auto_created=True)

    brand = models.CharField('Марка автомобиля', max_length=250)

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = 'Марка автомобиля'
        verbose_name_plural = 'Марки автомобилей'

