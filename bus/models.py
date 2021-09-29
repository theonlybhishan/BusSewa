from django.db import models
from datetime import datetime
# from django.db.models.base import ModelState

# from django.utils import tree
# from booking.models import Seat


class Amneties(models.Model):
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
class Seat(models.Model):
    bus= models.ForeignKey('Bus',on_delete= models.CASCADE, default=1)
    seat_no= models.IntegerField()
    occupant_firstname= models.CharField(max_length=200)
    occupant_lastname =models.CharField(max_length=200)
    occupant_email= models.EmailField(max_length=255)
    purchase_time= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"#{self.seat_no}{self.occupant_firstname}-{self.occupant_lastname}"


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
    bus_name        =models.CharField(max_length=200)
    # slug            =models.SlugField(max_length = 200, unique=True)
    bustype         =models.CharField(max_length=100, choices=BUS_TYPE)
    route           =models.ForeignKey(Route, on_delete=models.CASCADE)
    no_seats        =models.IntegerField()
    bus_image       =models.ImageField(upload_to='photos/photo',blank=True)
    operator        =models.ForeignKey(Agent, on_delete=models.CASCADE)
    boarding_time   =models.TimeField()
    end_time        =models.TimeField()
    duration        =models.IntegerField(blank=True)
    amneties        =models.ManyToManyField(Amneties, blank=True)
    discount        =models.IntegerField()
    created_date    =models.DateTimeField(auto_now_add=True)
    modified_date   =models.DateTimeField(auto_now=True)
    bus_number      =models.CharField(max_length=100)
    driver_name     =models.CharField(max_length=100)
    seat_type       =models.CharField(max_length=100, choices=SEAT_TYPE)
    no_seats        =models.IntegerField(default=40)
    booked_seat     =models.ManyToManyField('Booking_seat', blank=True, default=1)
    date            =models.DateField(auto_now=False, auto_now_add=False, default=datetime.now)
    price           =models.IntegerField()
    is_active       =models.BooleanField(default= False)
    def __str__(self):
        return self.bus_name


class Booking_seat(models.Model):
    seat_no = models.ForeignKey(Seat, on_delete=models.CASCADE, default=1)
    book_id= models.CharField(max_length=250, blank=True)
    date_added=models.DateField(auto_now_add=False)


    def __str__(self):
        return f'{self.seat_no}{self.book_id}'