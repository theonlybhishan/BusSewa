# Generated by Django 3.2.7 on 2021-09-30 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0003_auto_20210930_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='seat_type',
            field=models.CharField(choices=[('1*1', '1*1'), ('3*3', '3*3'), ('1*2', '1*2'), ('2*3', '2*3'), ('2*2', '2*2'), ('3*2', '3*2'), ('2*1', '2*1')], max_length=100),
        ),
    ]
