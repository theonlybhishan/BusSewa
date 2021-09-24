from django.urls import path
from .views import booking
# Create your views here.
urlpatterns=[
    path('', booking, name='booking')
]