# Generated by Django 3.2.7 on 2022-09-16 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0002_alter_bus_seat_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='seat_type',
            field=models.CharField(choices=[('3*2', '3*2'), ('3*3', '3*3'), ('1*1', '1*1'), ('1*2', '1*2'), ('2*1', '2*1'), ('2*3', '2*3'), ('2*2', '2*2')], max_length=100),
        ),
    ]