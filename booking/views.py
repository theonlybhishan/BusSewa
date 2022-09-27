from multiprocessing import context
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from hotel.models import Hotels, Rooms
from bus.models import *
from booking.models import BookedHotel, Cart, CartItem
from .forms import *

# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    print("cart_id",cart)
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, hotel_id):
    room = request.GET['room']
    hotel = Hotels.objects.get(id=hotel_id) #get_hotel
    variation=[]
    # bus = Bus.objects.get(id=bus_id)
    # print("***************************",bus)
    # bus= Bus.objects.get(id= bus_id)
    # print(bus)
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))

    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save()
    try:
        cart_item = CartItem.objects.get(product = hotel, cart= cart)
        cart_item.quantity = 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item= CartItem.objects.create(
            product=hotel,
            quantity = 1,
            cart= cart,
        )
        cart_item.save()
        # return HttpResponse(cart_item.product)
    return redirect('cart')

def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_items = CartItem.objects.filter(cart = cart , is_active = True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        # tax = 0#(2*total)/100
        # grand_total = total+tax

    except ObjectDoesNotExist:
        pass #just ignore

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
    }

    return render(request,'bookings/cart.html', context)


def remove_cart_item(request, hotel_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Hotels, id=hotel_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart')


    # try:
    #     if request.user.is_authenticated:
    #         cart_item = CartItem.objects.get(product=product, user=request.user, id=cart_item_id)
    #     else:
    # except:
    #     pass
    # return redirect('cart')

# def hotelbooking(request):
#     user=request.user
#     form = BookedForm
#     context={
#         'form':form
#     }
#     return render(request, 'hotels/booking.html', context)

def hotelbooking(request, total=0, quantity=0, cart_items=None):
    user= request.user
    print(user)
    try:
        tax=0
        grand_total=0
        if request.user.is_authenticated:
            cart_items= CartItem.objects.filter(is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active= True)
        # cart = Cart.objects.get(cart_id=_cart_id(request))
        # cart_items = CartItem.objects.filter(cart=cart, is_active= True)
        for cart_item in cart_items:
            total += cart_item.product.price
            quantity += cart_item.quantity
        # tax= (2*total)/100
        grand_total = total + 0
    except ObjectDoesNotExist:
        pass

    context={
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
    }
    return render(request, 'hotels/booking.html',context)
