from django.contrib.auth.models import User
from django.db import models
# from django.db.models.base import Model
from accounts.models import Account
from bus.models import Bus, Seat
# Create your models here.

class Payment(models.Model):
    user = models.ForeignKey(Account ,on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    amount_paid = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.payment_id

class BookedSeat(models.Model):
    seat = models.ForeignKey(Seat,on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE)
    user    = models.ForeignKey(Account, on_delete=models.CASCADE)
    bus_id  =models.ForeignKey(Bus, on_delete=models.CASCADE)
    pickup_area = models.CharField(max_length=100,blank=True)
    drop_area =models.CharField(max_length=100, blank=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    phone_number = models.CharField(max_length=15, blank=True)


def __str__(self):
    return self.bus_id.bus_name


