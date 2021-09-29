# Generated by Django 3.2.7 on 2021-09-26 05:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_name', models.CharField(max_length=50, unique=True)),
                ('phone_number', models.IntegerField()),
                ('description', models.TextField(blank=True, max_length=255)),
                ('agent_image', models.ImageField(blank=True, upload_to='photos/agents')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('discount', models.IntegerField()),
                ('is_available', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Agent',
                'verbose_name_plural': 'Agents',
            },
        ),
        migrations.CreateModel(
            name='Amneties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='pickupPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_no', models.IntegerField()),
                ('occupant_firstname', models.CharField(max_length=200)),
                ('occupant_lastname', models.CharField(max_length=200)),
                ('occupant_email', models.EmailField(max_length=255)),
                ('purchase_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('start_point', models.CharField(blank=True, max_length=100)),
                ('end_point', models.CharField(blank=True, max_length=100)),
                ('distance', models.IntegerField()),
                ('is_active', models.BooleanField(default=False)),
                ('pickup_point', models.ManyToManyField(blank=True, to='bus.pickupPoint')),
            ],
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_name', models.CharField(max_length=200)),
                ('bustype', models.CharField(choices=[('AC', 'AC'), ('DELUXE', 'DELUXE'), ('NORMAL', 'NORMAL'), ('HIACE', 'HIACE'), ('JEEP', 'JEEP')], max_length=100)),
                ('bus_image', models.ImageField(blank=True, upload_to='photos/photo')),
                ('boarding_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('duration', models.IntegerField(blank=True)),
                ('discount', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('bus_number', models.CharField(max_length=100)),
                ('driver_name', models.CharField(max_length=100)),
                ('seat_type', models.CharField(choices=[('2*3', '2*3'), ('2*1', '2*1'), ('1*1', '1*1'), ('2*2', '2*2'), ('1*2', '1*2'), ('3*2', '3*2'), ('3*3', '3*3')], max_length=100)),
                ('no_seats', models.IntegerField(default=40)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('price', models.IntegerField()),
                ('is_active', models.BooleanField(default=False)),
                ('amneties', models.ManyToManyField(blank=True, to='bus.Amneties')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus.agent')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus.route')),
            ],
        ),
        migrations.CreateModel(
            name='Booking_seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(blank=True, max_length=250)),
                ('date_added', models.DateField()),
                ('seat_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bus.seat')),
            ],
        ),
        migrations.AddField(
            model_name='agent',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus.route'),
        ),
    ]
