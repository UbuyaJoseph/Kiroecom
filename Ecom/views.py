from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
import json
import datetime 
from .models import* 
from . utils import cookieCart, cartData, guestOrder
from django.contrib import messages
#from django.contrib.auth.models import user, auth

# Create your views here.

def Store(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all()
    context = {'products': products, 'cartItems':cartItems}
    return render(request, 'Ecom/Store.html', context)


def Cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']


    context = {'items':items, 'order':order, 'cartItems': cartItems}
    return render(request, 'Ecom/Cart.html', context)

def Checkout(request):
   
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems': cartItems }
    return render(request, 'Ecom/Checkout.html', context)


def updateItem(request):
    data = json.loads(request.body) 
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)
    print('am adding to cart!')


    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()


    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json .loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)



    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()


    if order.shipping == True:
        ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )
    return JsonResponse('payment complete!', safe=False)


def About(request):
    return render(request, 'Ecom/About.html')

def Contact(request):
    return render(request, 'Ecom/Contact.html')


def Men(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all()
    context = {'products': products, 'cartItems':cartItems}
    return render(request, 'Ecom/Men.html', context)


def Women(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all()
    context = {'products': products, 'cartItems':cartItems}
    return render(request, 'Ecom/Women.html', context)


def Children(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all()
    context = {'products': products, 'cartItems':cartItems}
    return render(request, 'Ecom/Children.html', context)






    