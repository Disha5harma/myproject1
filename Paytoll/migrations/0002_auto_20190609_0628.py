# Generated by Django 2.2.1 on 2019-06-09 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Paytoll', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car_detail',
            name='fuel_type',
        ),
        migrations.AddField(
            model_name='car_detail',
            name='diesel_fuel',
            field=models.BooleanField(default='True'),
        ),
        migrations.AlterField(
            model_name='car_detail',
            name='car_number',
            field=models.CharField(max_length=20),
        ),
    ]
