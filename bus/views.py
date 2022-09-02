#qs = Bus.objects.filter(route_name__start_point__iexact=start_point
from json.decoder import JSONDecodeError
from django.contrib.auth.models import User
from django.core.checks.messages import Error
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import response
from django.http.response import HttpResponse
from django.template.loader import render_to_string
from accounts.models import Account
from bus.models import Bus, Payment, PaymentIntent,Route, Seat
from django.shortcuts import redirect, render
from .forms import SeatBookingForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


# all views for bus

import uuid

from django.views.generic import TemplateView, View
from django.core import serializers
from django.conf import settings
import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
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
        'form':form,
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
    # print('============data==============',data)
    bus = Bus.objects.get(bus_name=data.get("busName"), pk = data.get("busId"))
    busID=bus.id
    # print('busID:',busID)
    # print('bus type',type(bus))
    bus_id= int(data.get("busId"))
    
    # print('bus_id',bus_id)
    # print('bus_id',type(bus_id))
    occupied = Seat.objects.filter(bus__pk=bus_id,is_booked=True,is_paid=True)
    # print("occupied type",type(occupied))

    # occupied_seat = serializers.serialize('json',occupied)
    #  occupied=occupied.append(booked_seats)
    # print('occupied seat_type:',occupied)
    occupied_seat = list(map(lambda seat : seat.bookedseat_no - 1, occupied))
    # occupied_seat = list(occupied)
    # print('occupied_seat:',occupied_seat)
    # print('occuied_seat_type',type(occupied))

    return JsonResponse({
        "occupied_seats":occupied_seat,
        "bus":str(bus),
        "busId":busID,
        
    })
    # return    

@csrf_exempt

def makePayment(request):
    print('****************************user**********',request.user.email)
    # form = SeatBookingForm(request.POST or None)
    # print(form)
    # data= {}
    # if request.is_ajax():
    #     print('xiryo---------------')
        # if form.is_valid():
            # form.save()
        # data['occupant_firstname']=form.cleaned_data.get('firstName')
        # data['occupant_lastname']=form.cleaned_data.get('lastName')
        # data['occupant_number']=form.cleaned_data.get('phoneNumber')
        # data['pickup_area']=form.cleaned_data.get('pickupArea')
        # data['drop_area']=form.cleaned_data.get('dropArea')
        # data['status']='ok'
        # print(data)

            # return JsonResponse("success")
        # else:
        #     print('error for is not saved')
    # else:
    #     print('request is not received')
    if request.method == 'POST':
        print("-------------------------- here----------------------")
        data = json.loads(request.body)
        print('payment ============data==============',data)
        seat_numbers = list(map(lambda seat:seat+1, data["seat_list"]))
        print("------------------",seat_numbers)
        
        bus_title =data["bus_title"]
        print('bus_title',bus_title)
        bus_id = int(data["bus_id"])
        print('busId:',type(bus_id))
        cost = Bus.objects.get(bus_name=bus_title, pk = bus_id).price
        print('cost',type(cost))
        totalAmount=int(cost*len(seat_numbers))/100
        print('totalTicketPrice',totalAmount)
        print('---------------',data['firstName'])
        bus = Bus.objects.get(id= bus_id),
        print("bus==================",bus)

        no_of_seats = len(seat_numbers)
        bus_obj = Bus.objects.all()
        bus = Bus.objects.get(id= bus_id),
        
        for no_seat in seat_numbers:
            print('no-of seats========',request.user,type(bus_obj),type(no_of_seats),data['firstName'],data['lastName'],
            data['pickupArea'],data['dropArea'],request.user.email,data['phoneNumber'])
            seat_obj = Seat.objects.create(
            user = Account.objects.get(pk = request.user.id),
            bookedseat_no = no_seat,
            bus = Bus.objects.get(id= bus_id),
            occupant_firstname = data['firstName'],
            occupant_lastname =data['lastName'],
            occupant_number=data['phoneNumber'],
            pickup_area=data['pickupArea'],
            drop_area=data['dropArea'],
            occupant_email= request.user.email,
            )        
            seat_obj.save()
            print('data saved============================================')
            #sending mail to user about ticket
        # print('user',user)
        current_site = get_current_site(request)
        mail_subject = 'your seet has been booked'
        message = render_to_string('accounts/seat_book_email.html',{
            'user':request.user,
            'domain': urlsafe_base64_encode(force_bytes(request.user.pk)),
            'token': default_token_generator.make_token(request.user),
        })
        to_email = request.user.email
        send_email = EmailMessage(mail_subject,message,to=[to_email])
        print(to_email)
        send_email.send()


        # return redirect('')
        # return JsonResponse({"bookedseat_no":"bookedseat_no"},safe=True)

                            



def token_generator():
    id=str(uuid.uuid4())
    return id

def esewa_payment(request):
    bus_id = request.GET.get('bus_id')
    # current_user = request.User
    print('bus_id',bus_id)
    token = token_generator()
    print('token===================================',token)
    booked_data= Bus.objects.get(pk=bus_id)
    print(booked_data)
    booked_price= Bus.objects.get(pk=bus_id).price
    print(booked_price)
    booked_seat = Seat.objects.filter(user=request.user, bus=booked_data, is_booked = False, is_paid=False)
    # print(booked_seat) 
    total_price = int(len(booked_seat)*booked_price)
    print('booked_seat==============',booked_seat)
    print('booked_data============',total_price)
    context={
        'booked_seat':booked_seat,
        'total_price':total_price,
        'token':token
    }
    return render(request, 'bus/esewa_payment.html',context)



def esewa_payment_success(request):
    oid = request.GET.get('oid')
    amt = request.GET.get('amt')
    pay_obj = Payment.objects.create(
        user= request.user,
        transection_id = oid,
        transection_amount = amt
    )
    print('=====================================',oid)
    print(request.user)
    print(amt)
    print('pay_obj*****************',pay_obj)
    pay_obj.save()
    print('Datasaved****************')
    seats = Seat.objects.filter(user= request.user, is_booked=False, is_paid=False)
    if seats.exists():
        for seat in seats:
            seat.is_paid = True
            seat.is_booked = True
            seat.save()
    context ={

    }
    messages.success(request, 'seat is booked')
    return redirect('/')



@login_required(login_url='login')
def Dashboard(request):
    booked = Seat.objects.filter(user = request.user, is_booked = True)
    # booked_bus = booked
    booked_count = booked.count()
    context={
        'booked_count': booked_count
    }
    return render(request, 'accounts/dashboard.html',context)


def my_booked(request):
    booked = Seat.objects.filter(user = request.user, is_booked = True)
    # booked = booked.bus.objects.all()
    # booked_bus = Bus.objects.filter
    booked_count= booked.count()
    

    context={
        'booked_count':booked_count,    
        'booked':booked
    }
    return render(request,'accounts/my_booked.html',context)

@login_required
def cancel_ticket(request):
    booked= Seat.objects.filter(user = request.user)
    # delete = booked.delete()
    context={
        'booked':booked
    }
    return render(request,'accounts/cancel_ticket.html',context)

def delete_ticket(request,pk):
    booked= Seat.objects.get(pk=pk)
    booked.delete()

    return redirect('/cancel_ticket/')

@staff_member_required
def admin_dashboard(request):
    getbus = Bus.objects.all()
    bus_count=int(getbus.count())
    # print('************************************dsdsdsdsd0s2dsd48sd415sd',bus_count)
    # seat = Seat.objects.filter(bus__pk = getbus.pk , bus__bus_name = getbus.bus_name)

    context={
        # 'seats':seat,
        'buses':getbus,
        'bus_count':bus_count
    }
    return render(request,'accounts/admin_dashboard.html',context)



def bus_profile(request,id):
    bus = Bus.objects.get(pk=id)
    print('******************* bus',bus)
    seat = Seat.objects.filter(bus__pk = id)
    print('******************************seat',seat)
    context={
        'pro_bus': bus,
        'seats':seat
    }

    return render(request,'accounts/bus_profile.html',context)