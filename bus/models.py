from pyexpat import model
from django.db import models
from datetime import datetime

from accounts.models import Account
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.core.exceptions import ValidationError

# from django.db.models.base import ModelState

# from django.utils import tree
# from booking.models import Seat


class Services(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class pickupPoint(models.Model):
    # route= models.ManyToManyField(Route)
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name 

class Route(models.Model):
    slug            =models.SlugField(max_length=200, blank=True)
    start_point     =models.CharField(max_length=100, blank=True)
    end_point       =models.CharField(max_length=100, blank=True)
    pickup_point    =models.ManyToManyField(pickupPoint, blank=True)
    distance        =models.IntegerField()
    is_active       =models.BooleanField(default=False)
    def __str__(self):
        return f'{self.start_point} - {self.end_point}'
    def boarding_place(self):
        return",".join([str(p) for p in self.pickup_point.all()])
    
    # def pickup_place(self):
    #     for p in self.pickup_point.all():
    #         return str(p)


  
# Create your models here.
class Agent(models.Model):
    agent_name      = models.CharField(max_length=50, unique=True)
    # slug            = models.CharField(max_length=100, unique=True)
    phone_number    = models.IntegerField()
    description     = models.TextField(max_length=255, blank=True)
    agent_image     = models.ImageField(upload_to='photos/agents',blank=True)
    route           = models.ForeignKey(Route, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    updated_date    = models.DateTimeField(auto_now_add=True)
    discount        = models.IntegerField()
    is_available    = models.BooleanField(default = False)

    class Meta:
        verbose_name = ("Agent")
        verbose_name_plural = ("Agents")

    def __str__(self):
        return self.agent_name

    # def get_absolute_url(self):
    #     return reverse("category_detail", kwargs={"pk": self.pk})

def seat_check(value):
    if value <= 40:
        return value
    else:
        raise ValidationError("Total number of seat on bus are only 40")

class Bus(models.Model):
    BUS_TYPE        =(
        ('AC','AC'),
        ('DELUXE','DELUXE'),
        ('NORMAL','NORMAL'),
        ('HIACE','HIACE'),
        ('JEEP','JEEP'),
    )

    SEAT_TYPE       ={
        ('1*1','1*1'),
        ('1*2','1*2'),
        ('2*1','2*1'),
        ('2*2','2*2'),
        ('3*2','3*2'),
        ('2*3','2*3'),
        ('3*3','3*3')

    }
    user = models.ForeignKey(Account,on_delete=models.CASCADE, null=True)
    bus_name        =models.CharField(max_length=200)
    bus_id          = models.IntegerField(unique=True, default=True)
    # slug            =models.SlugField(max_length = 200, unique=True)
    bustype         =models.CharField(max_length=100, choices=BUS_TYPE)
    route           =models.ForeignKey(Route, on_delete=models.CASCADE)
    bus_image       =models.ImageField(upload_to='photos/photo',blank=True)
    operator        =models.ForeignKey(Agent, on_delete=models.CASCADE)
    boarding_time   =models.TimeField()
    end_time        =models.TimeField()
    duration        =models.IntegerField(blank=True)
    amneties        =models.ManyToManyField(Services, blank=True)
    discount        =models.IntegerField()
    created_date    =models.DateTimeField(auto_now_add=True)
    modified_date   =models.DateTimeField(auto_now=True)
    bus_number      =models.CharField(max_length=100)
    driver_name     =models.CharField(max_length=100)
    seat_type       =models.CharField(max_length=100, choices=SEAT_TYPE)
    no_seats        =models.IntegerField(default=40)
    booked_seat     =models.ManyToManyField('Seat', blank=True, default=[0], related_name= "booking-seat+")
    date            =models.DateField(auto_now=False, auto_now_add=False, default=datetime.now)
    price           =models.IntegerField()
    rating           =models.IntegerField(default=2)
    is_active       =models.BooleanField(default= False)
    def __str__(self):
        return f'{self.bus_id}.{self.bus_name}=>{self.route}'
    

class Seat(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE, null=True)
    bus= models.ForeignKey(Bus,on_delete= models.CASCADE,null= True, blank= True)
    seat_no= models.IntegerField(blank=True, null=True)
    bookedseat_no =models.IntegerField(blank=True, null=True,validators =[seat_check])
    occupant_firstname= models.CharField(max_length=200)
    occupant_lastname =models.CharField(max_length=200)
    occupant_number = models.CharField(max_length=100, blank=True)
    pickup_area =models.CharField(max_length=100, blank=True)
    drop_area = models.CharField(max_length=100, blank=True)
    occupant_email= models.EmailField(max_length=255)
    purchase_time= models.DateTimeField(auto_now_add=True)
    # book_id= models.CharField(max_length=250, blank=True)
    date_added=models.DateTimeField(auto_now_add=True)
    # datetime_booked = models.DateTimeField()
    is_booked = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.bookedseat_no}'


class Seatdetail(models.Model):
    # seat = models.ForeignKey(Seat, models.CASCADE, null=True, blank=True)
    seat_no = models.IntegerField(blank=True)
    seat_name = models.CharField(blank=True, max_length=10)
    lastseat  = models.BooleanField(default=False)
    last_seat_no = models.PositiveIntegerField(default=30)
    first_seat = models.BooleanField(default=False)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    seat = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f'{self.seat}.{self.seat_no}=>{self.seat_name}'



# class Booking_seat(models.Model):
#     seat_no = models.ForeignKey(Seat, on_delete=models.CASCADE, default=1)
#     book_id= models.CharField(max_length=250, blank=True)
#     date_added=models.DateField(auto_now_add=False)


#     def __str__(self):
#         return f'{self.seat_no}{self.book_id}'

class PaymentIntent(models.Model):
    referrer = models.URLField()
    bus_title = models.CharField(max_length=255)
    bus_id = models.IntegerField()
    seat_numbers = models.CharField(max_length=200)


class Payment(models.Model):
    user= models.ForeignKey(Account, on_delete=models.CASCADE, related_name='payment_name') 
    transection_id = models.CharField(max_length=255)
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
    product = models.ForeignKey(Bus, on_delete=models.CASCADE)
    quantity = models.IntegerField( default=0)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)
    
