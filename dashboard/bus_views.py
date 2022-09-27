from multiprocessing import context
from django.shortcuts import render, redirect
from dashboard.bus_forms import *
from dashboard.forms import *
from bus.models import *


def Addbus(request):
    user= request.user
    forms=BusForm
    if request.POST:
        forms = BusForm(request.POST, request.FILES)
        print(request.FILES)
        if forms.is_valid():
            obj = forms.save(commit=False)
            obj.user = user
            obj.save()
            
        return redirect('all_bus')
    context = {
        'form': forms
    }
    return render(request, 'dashboard/addbus.html',context)


def AddSeat(request):
    user= request.user
    bus = Bus.objects.filter(user=user)
    print('bus',bus)
    print('user',user)
    forms = SeatForm(bus)

    if request.POST:
        forms = SeatForm(bus ,request.POST, request.FILES)
        print(request.FILES)
        if forms.is_valid():
            print(forms)
            obj = forms.save(commit=False)
            obj.user = user
            obj.save()
            
        return redirect('all_bus')
    context = {
        'form': forms
    }
    return render(request, 'dashboard/bus/add_seat.html',context)


def AddseatDetail(request):
    user= request.user
    bus = Bus.objects.filter(user=user)  
    forms = AddSeatForm
    context = {
        'form': forms
    }
    return render(request, 'dashboard/addbus.html',context)


def AddRoute(request):
    forms = RouteForm
    if request.POST:
        forms = RouteForm(request.POST, request.FILES)
        print(request.FILES)
        if forms.is_valid():
            forms.save()
        return redirect('all_bus')
    context = {
        'form': forms
    }
    return render(request, 'dashboard/bus/add_route.html',context)


def deletebus(request,pk):
    # user= request.user
    # print('enter  into delete')
    # if user.role==1 or user.role==2:
    bus = Bus.objects.filter(pk=pk)
    bus.delete()

    return redirect('all_bus')

def Allbus(request):
    user= request.user
    if user.role==1:
        bus = Bus.objects.all()
    elif user.role==1 or user.role==2:
        bus = Bus.objects.filter(user=user, is_active=True)
    context={
        'bus':bus
    }
    return render(request, 'dashboard/bus/all_bus.html',context)


        
def Addagent(request):
    user= request.user
    forms = operatorForm
    if request.POST:
        forms = operatorForm(request.POST, request.FILES)
        print(forms)
        forms.save()
        return redirect('bus_dash')

    context ={
        'form':forms
    }
    return render(request, 'dashboard/bus/add_agent.html',context)


        
        # def AllBookedSeats(request):
#     user= request.user
#     if user.role==1:
#         bus = Bus.objects.all()
#     elif user.role==1 or user.role==2:
#         bus = Bus.objects.filter(user=user, is_active=True)
#         seat = Seat.objects.filter(user=user, is_active=True)
#     context={
#         'bus':bus
#     }
#     return render(request, 'dashboard/bus/all_bus.html',context)
