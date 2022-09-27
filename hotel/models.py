from django.db import models
# from bookings.models import Cities
from django.urls import reverse
from accounts.models import Account

# Create your models here.

"""
amneties
"""    
class Amneties(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256)
    image=models.ImageField(upload_to='amneties', blank=True, null=True)

    def __str__(self):
        return self.title

"""
complimentary models
"""
class Complimentary(models.Model):
    title = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    photos = models.ImageField(upload_to='complimentary', blank=True, null=True)

    def __str__(self):
        return self.title

"""
category models
"""
class Category(models.Model):
    title= models.CharField(max_length=100)
    slug = models.SlugField(max_length=256, blank=True, null=True)
    rooms_number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

"""
main model
"""
class Hotels(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE, null=True)
    title    = models.CharField(max_length=200)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(max_length=2000, blank=True)
    location        = models.URLField()
    image           = models.ImageField(upload_to='hotel', blank=True, null=True)
    # total           = models.IntegerField()
    room          = models.ForeignKey('Rooms', on_delete= models.CASCADE, related_name="hotel_room", null=True, blank=True)
    price           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    address         = models.CharField(max_length=256)
    phone_number    = models.CharField(max_length=16)
    city            = models.CharField(max_length=100, blank=True, null=True)
    # category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)
    # reviews         = models.models.IntegerField(_("   "))

    def get_url(self):
        return reverse('hotel-detail', args=[self.slug])

    def __str__(self):
        return self.title

    def no_rooms(self):
        return self.room


# class variation(models.Model):
#     hotel = models.models.ForeignKey(Hotels, verbose_name=("variation_categories"), on_delete=models.CASCADE) 

"""hotels rooms
""" 
class Rooms(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE, null=True)
    room_no = models.IntegerField(default=0)
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, default=None, blank=True)
    image = models.ImageField(upload_to='rooms', blank=True)
    room_type = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True, related_name='room_type')
    # room_tpe = models.ManyToManyField('Category', related_name="roomcategories")
    price = models.IntegerField()
    amneties = models.ManyToManyField(Amneties, related_name="allamneties")
    size = models.IntegerField()
    compimentary = models.ManyToManyField(Complimentary, default=None, blank=True)
    number= models.PositiveSmallIntegerField(default=0)
    is_available = models.BooleanField(default=False)
    is_booked = models.BooleanField(default= False)

    # category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='room_type')

    def __str__(self):
        return self.room_type.title

"""
hotel gallery
"""
class HotelGallery(models.Model):
    hotels = models.ForeignKey(Hotels, default=None, on_delete=models.CASCADE)
    rooms = models.ForeignKey('Rooms', default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hotel', max_length=255)

    class Meta:
        verbose_name = 'Hotel Gallery'
        verbose_name_plural = 'Hotel Gallery'


class HotelBooking(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE, null=True)
    hotels = models.ForeignKey(Hotels, default=None, on_delete=models.CASCADE)
    # room_type = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True, related_name='room_type')
    price = models.IntegerField()

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return f'{self.hotels.title} =>{self.price}'
