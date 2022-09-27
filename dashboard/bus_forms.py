from dataclasses import fields
from django.forms import ModelForm
from bus.models import *


class BusForm(ModelForm):
    # def __init__(self, bus, *args, **kwargs):
    #     super(SeatForm,self).__init__(*args, **kwargs)
    #     self.fields['route'].queryset = bus

    class Meta:
        model = Bus
        exclude = ('user',)  #ETA: added comma to make this a tuple

        # fields = ('bus_name', 'bustype', 'route', 'bus_image',
        #  'operator', 'occupant_number', 'boarding_time', 'end_time',
        #   'duration', 'amneties', 'bus_number','discount','driver_name','seat_type',
        #   'no_seats','booked_seat','date','price','is_active',)



class SeatForm(ModelForm):
    def __init__(self, bus, *args, **kwargs):
        super(SeatForm,self).__init__(*args, **kwargs)
        self.fields['bus'].queryset = bus
    class Meta:
        model = Seat
        fields = ('bus', 'seat_no', 'bookedseat_no', 'occupant_firstname',
         'occupant_lastname', 'occupant_number', 'pickup_area', 'drop_area',
          'occupant_email', 'is_booked', 'is_paid',)


class AddSeatForm(ModelForm):

    class Meta:
        model = Seatdetail
        fields = '__all__'


class RouteForm(ModelForm):

    class Meta:
        model = Route
        fields = '__all__'

class operatorForm(ModelForm):

    class Meta:
        model = Agent
        fields = '__all__'

