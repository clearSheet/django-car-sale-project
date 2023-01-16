from django.contrib import admin

# Register your models here.
from .models import Card_Cars
from .models import Model_and_Brand_Cars

admin.site.register(Card_Cars)
admin.site.register(Model_and_Brand_Cars)