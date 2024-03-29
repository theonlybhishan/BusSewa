# Generated by Django 3.2.7 on 2022-09-19 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0005_auto_20220919_2000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat',
            name='seat',
        ),
        migrations.AddField(
            model_name='seatdetail',
            name='seat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bus.seat'),
        ),
        migrations.AlterField(
            model_name='bus',
            name='seat_type',
            field=models.CharField(choices=[('3*3', '3*3'), ('1*2', '1*2'), ('2*3', '2*3'), ('1*1', '1*1'), ('2*1', '2*1'), ('3*2', '3*2'), ('2*2', '2*2')], max_length=100),
        ),
    ]
