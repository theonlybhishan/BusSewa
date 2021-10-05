from django.db.models import fields
from django.forms import widgets
from bus.models import Seat
from django import forms
# from django.db import models
# from accounts.models import Account


class SeatBookingForm(forms.ModelForm):
    class Meta:
        model = Seat
        fields = ['occupant_firstname', 'occupant_lastname', 'occupant_number', 'pickup_area','drop_area']
        widgets = {
            'occupant_firstname':forms.TextInput(attrs={'class':'form-control', 'id':'firstnameid'}),
            'occupant_lastname':forms.TextInput(attrs={'class':'form-control', 'id':'lastnameid'}),
            'occupant_number':forms.TextInput(attrs={'class':'form-control', 'id':'phonenum'}),
            'pickup_area':forms.TextInput(attrs={'class':'form-control', 'id':'pickuparea'}),
            'drop_area':forms.TextInput(attrs={'class':'form-control', 'id':'droparea'}),
        }