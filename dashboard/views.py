from django.shortcuts import render, redirect

from dashboard.forms import *
from hotel.models import *
# Create your views here.

def dashboard(request):
    return render(request, 'dashboard/index.html')

def tables(request):
    return render(request, 'dashboard/tables.html')


def admin_login (request):
    return render(request,'dashboard/login.html')

def bus(request):
    book_seat = 0
    bus= Bus.objects.all()
    for bus in bus:
        print('bus', bus)
        booked_seat= Seat.objects.filter(bus=bus).count()
        book_seat += booked_seat

        print('book_seat', book_seat)
    
    print('total booked_seat',book_seat)
   
    context={
        'bus':bus,
        'book_seat':book_seat
    }
    return render(request,'dashboard/bus/bus_dash.html', context)

def hotel(request):
    user= request.user
    if user.role==1:
        hotel = Hotels.objects.all()
    elif user.role==1 or user.role==2:
        hotel = Hotels.objects.filter(user=user, is_available=True)

    context={
        'hotel':hotel
    }
    return render(request,'dashboard/hotel/hotel_dash.html',context)


def AddRoom(request):
    user=request.user
    hotel = Hotels.objects.filter(user=user, is_available=True)
    forms = RoomFrom(hotel)
    # forms = RoomFrom
    context = {
        'form': forms
    }
    return render(request, 'dashboard/add_room.html',context)

def Addhotel(request):
    user= request.user
    forms=HotelForm
    if request.POST:
        forms = HotelForm(request.POST, request.FILES)
        print(request.FILES)
        if forms.is_valid():
            obj = forms.save(commit=False)
            obj.user = user
            obj.save()

        return redirect('all_hotel')
    context = {
        'form': forms
    }
    return render(request, 'dashboard/add_hotel.html',context)


def hotelgallery(request):
    # user=request.user
    # hotel = Hotels.objects.get(user=user, is_available=True)
    # i=hotel.count()
    # print('i',i)
    # for hotel in 
    # rooms = Rooms.objects.filter(hotel=hotel)
    # print('Hotel',hotel)
    # print('Rooms',rooms)
    forms = GalleryForm
    context = {
        'form': forms
    }
    return render(request, 'dashboard/hotel/add_galleries.html',context)

def Allhotel(request):
    user= request.user
    if user.role==1:
        hotel = Hotels.objects.all()
    elif user.role==1 or user.role==3:
        hotel = Hotels.objects.filter(user=user, is_available=True)
    context={
        'hotel':hotel
    }
    return render(request, 'dashboard/hotel/all_hotel.html',context)


def AllRooms(request):
    user= request.user
    if user.role==1:
        hotel = Rooms.objects.all()
        print(hotel)
    elif user.role==1 or user.role==3:
        hotel = Rooms.objects.filter(user=user)
    context={
        'rooms':hotel,
    }
    return render(request, 'dashboard/hotel/all_rooms.html',context)


def hotel_room_detail(request, hotel_slug):
    hotel = Hotels.objects.filter(slug= hotel_slug)
    room = Rooms.objects.filter(hotel__slug=hotel)

    context = {
        'hotel':hotel
    }


