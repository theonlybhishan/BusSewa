from django.urls import path
from .import views
from . import bus_views

urlpatterns = [
    path('', views.dashboard, name="addashboard"),
    path('table/', views.tables, name="tables"),
    path('login_admin/', views.admin_login, name="login_admin"),
    path('bus/', views.bus, name="bus_dash"),
    path('hotel_dash/', views.hotel, name="hotel_dash"),




    #hotel_section
    path('add_hotel/', views.Addhotel, name="add_hotel"),
    path('add_room/', views.AddRoom, name="add_room"),
    path('galleries/', views.hotelgallery, name="add_gallery"),
    path('all_hotel/', views.Allhotel, name="all_hotel"),
    path('all_room/', views.AllRooms, name="all_rooms"),
    path('all_hotel/<str:slug>', views.hotel_room_detail, name = 'hotel_detail'),


    #bus_section
    path('add_bus/', bus_views.Addbus, name="add_bus"),
    path('delete_bus/<int:pk>', bus_views.deletebus, name="delete_bus"),
    path('all_bus/', bus_views.Allbus, name="all_bus"),
    path('add_seat/', bus_views.AddSeat, name="add_seat"),
    path('add_route/', bus_views.AddRoute, name="add_route"),
    path('add_bus_agent/', bus_views.Addagent, name="add_busagent"),
        

]
