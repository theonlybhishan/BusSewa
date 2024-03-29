# Generated by Django 3.2.7 on 2022-09-20 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0011_auto_20220920_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='seatdetail',
            name='first_seat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='seatdetail',
            name='lastseat',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='bus',
            name='seat_type',
            field=models.CharField(choices=[('3*2', '3*2'), ('2*2', '2*2'), ('3*3', '3*3'), ('2*1', '2*1'), ('2*3', '2*3'), ('1*1', '1*1'), ('1*2', '1*2')], max_length=100),
        ),
    ]
