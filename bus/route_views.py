from bus.serializers import *
from rest_framework.permissions import IsAuthenticated,IsAdminUser,BasePermission
from rest_framework.response import Response
from rest_framework import viewsets,permissions
from bus.models import *


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


class ServiceApi(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = Serviceserializer
    permission_classes = [writeonlyBusAdminPermission]


class PickuppointeApi(viewsets.ModelViewSet):
    queryset = pickupPoint.objects.all()
    serializer_class = pickuppointserializer
    permission_classes = [writeonlyBusAdminPermission]

class RouteApi(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = pickuppointserializer
    permission_classes = [writeonlyBusAdminPermission]

class AgentApi(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = Agentserializer
    permission_classes = [writeonlyBusAdminPermission]

class BusApi(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = Busserializer
    permission_classes = [writeonlyBusAdminPermission]

class SeatdetailApi(viewsets.ModelViewSet):
    queryset = Seatdetail.objects.all()
    serializer_class = Seatdetailserializer
    permission_classes = [writeonlyBusAdminPermission]

class SeatApi(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = Seatserializer
    permission_classes = [writeonlyBusAdminPermission]

class PaymentIntentApi(viewsets.ModelViewSet):
    queryset = PaymentIntent.objects.all()
    serializer_class = PaymentIntentserializer
    permission_classes = [writeonlyBusAdminPermission]

class PaymentApi(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = Paymentserializer
    permission_classes = [writeonlyBusAdminPermission]