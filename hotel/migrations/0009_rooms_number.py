# Generated by Django 3.2.7 on 2022-09-23 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0008_hotelbooking'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='number',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]