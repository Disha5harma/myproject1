# Generated by Django 2.2.1 on 2019-06-08 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='car_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_type', models.CharField(max_length=500, null=True)),
                ('car_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Paytoll.car_detail')),
            ],
        ),
    ]
