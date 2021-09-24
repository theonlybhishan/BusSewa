from django import forms
from django.forms import fields
from .models import Account


class RegistrationForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                'placeholder': 'Enter password',
                'class': 'form-control'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
                'placeholder':'confirm password',
                'class': 'form-control'
    }))

    class Meta:
        model= Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    def __init__(self,*args, **kwargs):
        super(RegistrationForms, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder']= 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder']= 'Enter Last Name'
        self.fields['phone_number'].widget.attrs['placeholder']= 'Enter Phonenumber'
        self.fields['email'].widget.attrs['placeholder']= 'Enter Email Address'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data= super(RegistrationForms, self).clean()
        password= cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')


        if password != confirm_password:
            raise forms.ValidationError(
                "password doesnot match!"
            )
