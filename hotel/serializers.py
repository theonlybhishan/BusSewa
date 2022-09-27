from rest_framework import serializers
from hotel.models import *


class Amnetiesserializer(serializers.ModelSerializer):
    class Meta:
        model = Amneties
        fields = '__all__'
        
class Complimentaryserializer(serializers.ModelSerializer):
    class Meta:
        model = Complimentary
        fields = '__all__'
        
class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class Hotelserializer(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields = '__all__'
        
class HotelGalleryserializer(serializers.ModelSerializer):
    class Meta:
        model = HotelGallery
        fields = '__all__'
        
class Roomserializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'
        
        