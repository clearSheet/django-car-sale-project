# Generated by Django 4.1.5 on 2023-01-16 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_card_cars_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model_and_Brand_Cars',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=250, verbose_name='Модель автомобиля')),
                ('brand', models.CharField(max_length=250, verbose_name='Марка автомобиля')),
            ],
            options={
                'verbose_name': 'Марка и модель автомобиля',
                'verbose_name_plural': 'Марки и модели автомобилей',
            },
        ),
    ]