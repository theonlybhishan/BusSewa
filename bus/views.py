#qs = Bus.objects.filter(route_name__start_point__iexact=start_point
from django.http.response import HttpResponse
from bus.models import Bus,Route, Seat
from django.shortcuts import render
from .forms import SeatBookingForm


from django.views.generic import TemplateView, View
from django.core import serializers

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
    bus=Bus.objects.filter(bus_name="Agni Yatayat", pk=1)
    print('bus:',bus)
    booked_seat = Seat.objects.filter(bus__bus_id=5)
    print('booked-seats:',type(booked_seat))
    return render(request, 'bus/home.html')
def test(request):
    return render(request, 'bus/test.html')
def bus(request):
    qs=Bus.objects.filter(is_active=True)
    startPoint_query=request.GET.get("startpoint")
    endPoint_query =request.GET.get("endpoint")
    departure_query=request.GET.get("departure")
    print('startPoint_query:',startPoint_query)
    print('endPoint_query:',endPoint_query)
    print('departure_query:',departure_query)
    form = SeatBookingForm()
    if startPoint_query !='' and startPoint_query is not None and startPoint_query !=''and endPoint_query is not None:
        qs = Bus.objects.filter(route__start_point__icontains= startPoint_query, route__end_point__icontains= endPoint_query, is_active=True)
        # place= 
        print(qs)
    # pickup_point=Bus.objects.filter(route__pickup_point__name)
    # if endPoint_query !='' and endPoint_query is not None:
    #     qs= Bus.objects.filter(route_name__end_point__icontains= endPoint_query)
    #     print(qs)
    # if departure_query !='' and departure_query is not None:
    #     qs = Bus.objects.filter(date__gte = departure_query)
    # data= json.loads(request.body)
    # print('============data==============',data)
    no_of_seat=40
    data=[]
    for x in range(1, 40):
        data.append(x)

    range1 = 10
    range2 = 4
    context={
        'bus':qs,
        'data':data,
        'range1':range1,
        'range2':range2,
    }
    return render(request, 'bus/bus.html',context)

class FilterView(View):
    def get(self ,request):
        qs=Bus.objects.all()
        seat = Seat.objects.all()
        data = serializers.serialize('json',qs)
        seat_data = serializers.serialize('json',seat)

        return JsonResponse({'data':data, 'seat_data':seat_data}, safe = False)

@csrf_exempt
def occupiedSeats(request):
    data= json.loads(request.body)
    print('============data==============',data)
    bus = Bus.objects.get(bus_name=data.get("busName"), pk = data.get("busId"))
    busID=bus.id
    print('busID:',busID)
    print('bus type',type(bus))
    bus_id= int(data.get("busId"))
    
    print('bus_id',bus_id)
    print('bus_id',type(bus_id))
    occupied = Seat.objects.filter(bus__pk=bus_id)
    print("occupied type",type(occupied))

    # occupied_seat = serializers.serialize('json',occupied)
    #  occupied=occupied.append(booked_seats)
    # print('occupied seat_type:',occupied)
    occupied_seat = list(map(lambda seat : seat.bookedseat_no, occupied))
    # occupied_seat = list(occupied)
    print('occupied_seat:',occupied_seat)
    # print('occuied_seat_type',type(occupied))

    return JsonResponse({
        "occupied_seats":occupied_seat,
        "bus":str(bus),
        "busId":busID,
        
    })
    # return    