from django.urls import path, include
from booking.models import BookedHotel
from hotel import views
from . import route_views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'amneties', route_views.AmnetiesApi,basename = "amnetieapi"),
router.register(r'complimentary', route_views.ComplimentaryApi,basename = "complimentaryapi"),
router.register(r'hotels', route_views.HotelsApi,basename = "hotelapi"),
router.register(r'category', route_views.CategoryApi,basename = "categoryapi"),
router.register(r'hotelgallery', route_views.HotelGalleryApi,basename = "hotelgallery"),
router.register(r'rooms', route_views.RoomsApi,basename = "roomapi"),

urlpatterns = [
    path('', views.home, name='hotel'),
    path('hotel-in/', views.hotel, name='searchhotel'),
    path('hotel-detail/<slug:hotel_slug>', views.hotel_detail, name='hotel-detail'),
    path('apis/hotel/',include(router.urls)),
    # path('placeorder/', hotelbooking, name='place-order'),

]
