from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('bus/', views.bus, name='bus'),
    path('occupied/', views.occupiedSeats, name='occupied-seat'),
]
