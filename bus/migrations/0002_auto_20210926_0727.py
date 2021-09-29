# Generated by Django 3.2.7 on 2021-09-26 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='booked_seat',
            field=models.ManyToManyField(blank=True, to='bus.Seat'),
        ),
        migrations.AlterField(
            model_name='booking_seat',
            name='seat_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus.seat'),
        ),
        migrations.AlterField(
            model_name='bus',
            name='seat_type',
            field=models.CharField(choices=[('2*1', '2*1'), ('1*2', '1*2'), ('1*1', '1*1'), ('3*3', '3*3'), ('3*2', '3*2'), ('2*2', '2*2'), ('2*3', '2*3')], max_length=100),
        ),
    ]
