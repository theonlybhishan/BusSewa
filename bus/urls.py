import json
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('test/', views.test , name='test'),
    path('bus/', views.bus, name='bus'),
    path('occupied/', views.occupiedSeats, name='occupied-seat'),
    path('data-json/', views.FilterView.as_view(), name='data-json')
]
