# Generated by Django 3.2.7 on 2022-09-27 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0011_rooms_is_booked'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='room_no',
            field=models.IntegerField(default=0),
        ),
    ]
