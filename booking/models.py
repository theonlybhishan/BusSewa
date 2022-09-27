from django.contrib.auth.models import User
from django.db import models
# from django.db.models.base import Model
from accounts.models import Account
from bus.models import Bus, Seat

# for hotels
from django.db.models.signals import pre_save
from hotel.models import Hotels, Rooms
from core.utils import unique_slug_generator

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



class BookedHotel(models.Model):
    hotel = models.ForeignKey(Hotels,on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE)
    user    = models.ForeignKey(Account, on_delete=models.CASCADE)
    room  =models.ForeignKey(Rooms, on_delete=models.CASCADE)
    check_in = models.CharField(max_length=100,blank=True)
    check_out =models.CharField(max_length=100, blank=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    phone_number = models.CharField(max_length=15, blank=True)
    is_booked = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)

# for hotels
"""
models for cities
"""

class Cities(models.Model):
    title = models.CharField(max_length=200)
    slug  = models.SlugField(max_length=200, blank=True)
    is_active = models.BooleanField(default=False)


    class Meta:
        verbose_name = ("city")
        verbose_name_plural = ("cities")

    def __str__(self):
        return self.title

"""models for review ratings"""
class ReviewRating(models.Model):
    # product = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField(default=0)
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.subject

"""
models for coupon
"""
class Coupon(models.Model):
    # coupon_id= models.IntegerField()
    coupon_name = models.CharField(max_length=256, blank=True)
    time = models.DateTimeField(auto_now=False, auto_now_add=False)
    price = models.PositiveIntegerField(blank= True, null=True)
    is_active = models.BooleanField(default=False)

"""
models for coupon
"""
class Offer(models.Model):
    offer_title = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now=False, auto_now_add=False)
    is_active = models.BooleanField(default=False)
    
# class PaymentIntent(models.Model):
#     referrer = models.URLField()
#     bus_title = models.CharField(max_length=255)
#     bus_id = models.IntegerField()
#     seat_numbers = models.CharField(max_length=200)

"""
models for Payment
"""
class Payments(models.Model):
    # user= models.ForeignKey(Account, on_delete=models.CASCADE, related_name='payment_name') 
    transection_id = models.CharField(max_length=255)
    # status = models.CharField(max_length=100)
    # payment_method = models.CharField(max_length=100)
    transection_amount= models.DecimalField(max_digits=8,decimal_places=2)


    def __str__(self):
        return f'{self.transection_id}{self.transection_amount}'

class Cart(models.Model):
    cart_id= models.CharField(max_length= 250, blank= True)
    date_added = models.DateField(auto_now=True)

    def __str__(self):
        return self.cart_id
    

class CartItem(models.Model):
    # user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    quantity = models.IntegerField( default=0)
    # variations = models.ManyToManyField(Variation, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity

    def __unicode__(self):
        return self.product


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        print(instance.title)
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Cities)

