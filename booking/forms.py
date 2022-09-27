from django.forms import ModelForm
from booking.models import BookedHotel
from hotel.models import *

class BookedForm(ModelForm):
    
    class Meta:
        model = BookedHotel
        exclude = ('user',)