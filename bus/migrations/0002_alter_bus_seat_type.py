# Generated by Django 3.2.7 on 2022-09-11 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='seat_type',
            field=models.CharField(choices=[('1*2', '1*2'), ('3*2', '3*2'), ('2*3', '2*3'), ('2*1', '2*1'), ('1*1', '1*1'), ('3*3', '3*3'), ('2*2', '2*2')], max_length=100),
        ),
    ]
