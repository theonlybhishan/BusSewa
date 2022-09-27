from hotel.serializers import *
from rest_framework.permissions import IsAuthenticated,IsAdminUser,BasePermission
from rest_framework.response import Response
from rest_framework import viewsets,permissions
from hotel.models import *


class writeByonlySuperAdminPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method =='GET':
            return True
        try:
            user = request.user
            if request.method =='POST' or request.method == 'PUT' or request.method == 'DELETE' or request.method == 'PATCH':
                if user.role == 1:
                    return True
        except:
            return False

class writeonlyBusAdminPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method =='GET':
            return True
        try:
            user = request.user
            if request.method =='POST' or request.method == 'PUT' or request.method == 'DELETE' or request.method == 'PATCH':
                if user.role == 1 or user.role==2:
                    return True
        except:
            return False

class writeonlyHotelAdminPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method =='GET':
            return True
        try:
            user = request.user
            if request.method =='POST' or request.method == 'PUT' or request.method == 'DELETE' or request.method == 'PATCH':
                if user.role==1 or user.role==3:
                    return True
        except:
            return False

class writeonlyUserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method =='GET':
            return True
        try:
            user = request.user
            if request.method =='POST' or request.method == 'PUT' or request.method == 'DELETE' or request.method == 'PATCH':
                if user.role==1 or user.role==2 or user.role==3 or user.role==4:
                    return True
        except:
            return False


class AmnetiesApi(viewsets.ModelViewSet):
    queryset = Amneties.objects.all()
    serializer_class = Amnetiesserializer
    permission_classes = [writeonlyHotelAdminPermission]

    
class ComplimentaryApi(viewsets.ModelViewSet):
    queryset = Complimentary.objects.all()
    serializer_class = Complimentaryserializer
    permission_classes = [writeonlyHotelAdminPermission]

class CategoryApi(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Categoryserializer
    permission_classes = [writeonlyHotelAdminPermission]

class HotelsApi(viewsets.ModelViewSet):
    queryset = Hotels.objects.all()
    serializer_class = Hotelserializer
    permission_classes = [writeonlyHotelAdminPermission]


    
class HotelGalleryApi(viewsets.ModelViewSet):
    queryset = HotelGallery.objects.all()
    serializer_class = HotelGalleryserializer
    permission_classes = [writeonlyHotelAdminPermission]


    
class RoomsApi(viewsets.ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = Rooms
    permission_classes = [writeonlyHotelAdminPermission]
