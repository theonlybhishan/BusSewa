from django.forms import ModelForm
from hotel.models import *
from bus.models import *

class AmnetiesForm(ModelForm):
    
    class Meta:
        model = Amneties
        fields = '__all__'



class GalleryForm(ModelForm):
    # def __init__(self, hotel, room, *args, **kwargs):
    #     super(GalleryForm,self).__init__(*args, **kwargs)
    #     self.fields['hotels'].queryset = hotel
    #     self.fields['rooms'].queryset = room
    class Meta:
        model= HotelGallery
        fields = '__all__'
        # fields = ('hotels', 'image',)

class HotelForm(ModelForm):
    
    class Meta:
        model = Hotels
        fields = ('title', 'slug', 'description', 'location', 'image',
                 'room', 'price', 'is_available', 'address', 'phone_number', 'city',)

class RoomFrom(ModelForm):
    class Meta:
        model= Rooms
        exclude = ('user',)
    def __init__(self, hotel=None, *args, **kwargs):
        super(RoomFrom,self).__init__(*args, **kwargs)
        self.fields['hotel'].queryset = hotel
        # fields=('hotel','room_no', 'image', 'room_type', 'price', 'amneties',  'size', 'compimentary',)




# All the bus reservation required for bus is available here

# Route
#PickupPoint
#Seat
# Bus
#seatdetail
