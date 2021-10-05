import json
from django.urls import path
from . import views

urlpatterns = [
    #dashboard
    path('dashboard/',views.Dashboard, name='dashboard'),
    path('my_booked/',views.my_booked,name='my_booked'),
    path('cancel_ticket/', views.cancel_ticket, name='cancel_ticket'),
    path('delete_ticket/<int:pk>/', views.delete_ticket, name='delete_ticket'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('',views.home, name='home'),
    path('test/', views.test , name='test'),
    path('bus/', views.bus, name='bus'),
    path('occupied/', views.occupiedSeats, name='occupied-seat'),
    path('payment/', views.makePayment, name="payment"),
    path('esewa_payment/', views.esewa_payment, name="esewa_payment"),
    path('esewa_payment_success/', views.esewa_payment_success, name="esewa_payment_success"),
    path('data-json/', views.FilterView.as_view(), name='data-json')
]
