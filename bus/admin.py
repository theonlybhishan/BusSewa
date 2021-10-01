from django.contrib import admin
from .models import *

class BusAdmin(admin.ModelAdmin):
    list_display=('bus_name', 'route', 'price','discount', 'is_active')
    list_editable=('discount', 'is_active')

class SeatAdmin(admin.ModelAdmin):
    list_display=('bookedseat_no','bus','date_added')
    

admin.site.register(pickupPoint)
admin.site.register(Amneties)
admin.site.register(Route)
admin.site.register(Agent)
admin.site.register(Bus, BusAdmin)
admin.site.register(Seat, SeatAdmin)
# admin.site.register(Booking_seat)
