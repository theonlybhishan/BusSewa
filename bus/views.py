#qs = Bus.objects.filter(route_name__start_point__iexact=start_point
from bus.models import Bus,Route
from django.shortcuts import render

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

    context={
        'bus':qs
    }
    return render(request, 'bus/bus.html',context)

def filter(request):
    return