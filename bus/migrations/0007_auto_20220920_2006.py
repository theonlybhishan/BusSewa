# Generated by Django 3.2.7 on 2022-09-20 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bus', '0006_auto_20220919_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bus',
            name='seat_type',
            field=models.CharField(choices=[('3*2', '3*2'), ('2*1', '2*1'), ('1*1', '1*1'), ('2*2', '2*2'), ('3*3', '3*3'), ('2*3', '2*3'), ('1*2', '1*2')], max_length=100),
        ),
    ]
