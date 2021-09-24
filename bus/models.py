from django.db import models
from datetime import datetime
# from django.db.models.base import ModelState

from django.utils import tree



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

class Bus(models.Model):
    BUS_TYPE        =(
        ('AC','AC'),
        ('DELUXE','DELUXE'),
        ('NORMAL','NORMAL'),
        ('HIACE','HIACE'),
        ('JEEP','JEEP'),
    )
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
    no_seats        =models.IntegerField(default=40)
    date            =models.DateField(auto_now=False, auto_now_add=False, default=datetime.now)
    price           =models.IntegerField()
    is_active       =models.BooleanField(default= False)
    def __str__(self):
        return self.bus_name