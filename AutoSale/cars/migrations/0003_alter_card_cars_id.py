# Generated by Django 4.1.5 on 2023-01-08 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_card_cars_options_card_cars_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card_cars',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID объявления'),
        ),
    ]
