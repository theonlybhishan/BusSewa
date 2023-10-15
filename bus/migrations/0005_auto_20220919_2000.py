# Generated by Django 3.2.7 on 2022-09-19 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0004_auto_20220916_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='seat',
            field=models.ManyToManyField(blank=True, to='bus.Seatdetail'),
        ),
        migrations.AlterField(
            model_name='bus',
            name='seat_type',
            field=models.CharField(choices=[('2*3', '2*3'), ('2*1', '2*1'), ('3*3', '3*3'), ('2*2', '2*2'), ('1*1', '1*1'), ('1*2', '1*2'), ('3*2', '3*2')], max_length=100),
        ),
    ]