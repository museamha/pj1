# Generated by Django 5.0.7 on 2024-11-08 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_car_slug_alter_car_discr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
