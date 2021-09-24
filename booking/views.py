from django.shortcuts import render
from django.urls.conf import path
from django.urls.resolvers import URLPattern

def booking(request):
    return render(request, 'bus/booking.html')