from django.db.models import fields
from django.forms import widgets
from bus.models import Seat
from django import forms
from django.db import models
from accounts.models import Account


class SeatBookingForm(forms.ModelForm):
    class Meta:
        model = Seat
        fields = ['occupant_firstname', 'occupant_lastname', 'occupant_email']
        widgets = {
            'occupant_firstname':forms.TextInput(attrs={'class':'form-control', 'id':'firstnameid'}),
            'occupant_lastname':forms.TextInput(attrs={'class':'form-control', 'id':'lastnameid'}),
            'occupant_email':forms.TextInput(attrs={'class':'form-control', 'id':'emailid'}),
        }