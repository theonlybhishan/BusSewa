#qs = Bus.objects.filter(route_name__start_point__iexact=start_point
from django.http.response import HttpResponse
from bus.models import Bus,Route
from django.shortcuts import render
from .forms import SeatBookingForm
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
    return render(request, 'bus/home.html')

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

    context={
        'bus':qs,
        # 'form':form
    }
    return render(request, 'bus/bus.html',context)

def filter(request):
    return


# @csrf_exempt
def occupiedSeats(request):
    # data= json.loads(request.body)
    # print('============data==============',data)
    # bus = Bus.objects.get(bus_name=data["busName"])
    # occupied = Bus.booked_seats.all()
    # occupied_seat = list(map(lambda seat : seat.seat_no-1, occupied))

    # return JsonResponse({
    #     "occupied_seats":occupied_seat,
    #     "bus":str(bus)
    # })
    return