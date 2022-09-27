from rest_framework import serializers
from bus.models import *

class Serviceserializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class pickuppointserializer(serializers.ModelSerializer):
    class Meta:
        model = pickupPoint
        fields = '__all__'

class Routeserializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'

class Agentserializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'

class Busserializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'

class Seatdetailserializer(serializers.ModelSerializer):
    class Meta:
        model = Seatdetail
        fields = '__all__'

class Seatserializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'


class PaymentIntentserializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentIntent
        fields = '__all__'

class Paymentserializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'