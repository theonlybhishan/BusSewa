from django.urls import path, include
from booking import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_cart/<int:hotel_id>/', views.add_cart, name='add-cart'),
    path('remove_cart_item/<int:hotel_id>/', views.remove_cart_item, name='remove-cart-item'),
    path('booking/<int:hotel_id>/', views.remove_cart_item, name='remove-cart-item'),
    path('placeorder/', views.hotelbooking, name='place-order'),

]
