from django.contrib import admin

from hotel.models import Amneties, Category, Complimentary, HotelGallery, Hotels, Rooms

# Register your models here.

admin.site.register(Hotels)
admin.site.register(Amneties)
admin.site.register(HotelGallery)
admin.site.register(Complimentary)
admin.site.register(Category)
admin.site.register(Rooms)
