# Generated by Django 3.2.7 on 2022-09-24 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_bookedhotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookedhotel',
            name='is_booked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bookedhotel',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
