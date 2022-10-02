from django.shortcuts import render, redirect
from django.views.generic import View, UpdateView

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
    elif user.role==1 or user.role==3:
        hotel = Hotels.objects.filter(user=user, is_available=True)
    context={
        'hotel':hotel
    }
    return render(request,'dashboard/hotel/hotel_dash.html',context)


def AddRoom(request):
    user=request.user
    hotel = Hotels.objects.filter(user=user, is_available=True)
    forms = RoomFrom(hotel)
    print(forms)
    if request.POST:
        forms = RoomFrom(hotel, request.POST, request.FILES)
        print(request.FILES)
        if forms.is_valid():
            obj = forms.save(commit=False)
            obj.user = user
            obj.save()
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
    hotel = Hotels.objects.get(slug= hotel_slug)
    room = Rooms.objects.filter(hotel=hotel)
    # print('room', room)

    context = {
        'rooms':room
    }

    return render(request, 'dashboard/hotel/hotel_detail.html', context)

def get_hotel_slug(self):
    hotel = Hotels.objects.filter(slug=self)
    for title in hotel:
        slug = title.slug
        return slug

def update_room(request,hotel_slug, pk):
    user= request.user
    hotel = Hotels.objects.filter(slug=hotel_slug)
    print(hotel)
    # hotel_name = hotel.title
    # print("hotel_name", hotel_name)
    room = Rooms.objects.filter(pk= pk).first()
    # print('rooms', room.id)
    form = RoomFrom(hotel ,instance = room)

    hotel_slug = get_hotel_slug(hotel_slug)
    print('hotel_slug', hotel_slug)

    if request.POST:
        form = RoomFrom(hotel, request.POST,instance = room)
        if form.is_valid():
            form.save()
            return redirect('all_hotel')
        
    context = {
        'form':form,
        'hotel':hotel_slug,
        'room':room
    }

    return render(request, 'dashboard/hotel/update_room.html', context)





# class UpdateRoom(UpdateView):
#     template_name= 'dashboard/hotel/update_room.html'
#     from_class = RoomFrom
#     model = Rooms

#     def get_object(self, queryset=None):
#         hotel = 
#         obj = Rooms.objects.filter(pk=self.kwargs['id']).first()
#         return obj

