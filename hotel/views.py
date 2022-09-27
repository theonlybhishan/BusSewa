from django.shortcuts import render, redirect, get_object_or_404
from hotel.models import Hotels, Category, Rooms
# Create your views here.


def home(request, hotel_type=None):
    categories = None
    hotel=None
    if hotel_type != None:
        categories = get_object_or_404(Category, cat_slug= hotel_type)
        hotel = Hotels.objects.filter(category=categories, is_available=True)
        hotel_count = hotel.count()
    else:
        hotel = Hotels.objects.all().filter(is_available=True)
        hotel_count = hotel.count()
    context = {
        'hotels':hotel
        }
    return render(request, 'hotels/home.html',context)


def hotel(request):
    hotel = None
    qs=None
    hotel_count=None
    room_count=None

    location = request.GET.get("location")
    print('location:',location)

    if location !='' and location is not None:
        qs = Hotels.objects.filter(address__icontains=location)
        room= Rooms.objects.all()
        # amneties = 
        # print('amneties:',amneties)
        print('room:',room)
        room_count = room.count()
        print(room_count)
        hotel_count = qs.count()
        print(qs)
    context={
        'hotels':qs,
        'hotel_count':hotel_count,
        'room_count': room_count,
    }

    return render(request, 'hotels/hotels.html',context)

def check_booking(request, checkin, checkout, slug, room_count):
    qs = Hotels.objects.filter(
        checkin__lte=checkin,
        checkout__gte=checkout,
        slug = slug
    )

    if len(qs) >= room_count:
        return False

    return True


def hotel_detail(request, hotel_slug):
    hotel= Hotels.objects.get(slug = hotel_slug)
    room = Rooms.objects.filter(hotel__slug = hotel)
    room_count = room.count()
    print(hotel)

    context={
        'single_hotel':hotel,
        'room_count':room_count,
    }
    return render(request, 'hotels/hotel_detail.html', context)


# payment gateway

# class EsewaRequestView(View):
#     def get(self, request, *args, **kwargs):
#         order = 
#         context = {
#             "order": order
#         }
#         return render(request, "esewarequest.html", context)
    
# class hotelbooking(request):
#     hotel