# Generated by Django 3.2.7 on 2022-09-16 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0003_alter_bus_seat_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seatdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Seat_no', models.IntegerField(blank=True)),
                ('seat_name', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='bus',
            name='seat_type',
            field=models.CharField(choices=[('2*2', '2*2'), ('1*2', '1*2'), ('2*1', '2*1'), ('1*1', '1*1'), ('3*2', '3*2'), ('3*3', '3*3'), ('2*3', '2*3')], max_length=100),
        ),
    ]
