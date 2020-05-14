import stripe 
from django.conf import settings 
from django.views.generic.base import TemplateView
from django.shortcuts import render # new
from orders.models import Order
from cart.cart import Cart

stripe.api_key = settings.STRIPE_SECRET_KEY # new

# def HomePageView(request,order_id):
#     order = Order.objects.get(pk=order_id)
#     price = int(order.price)*100
#     context={
#         'key': settings.STRIPE_PUBLISHABLE_KEY,
#         'order': order,
#         'price':price
#     }
#     # context['key'] = 
#     # context['order'] =/ order
    
#     return render(request, 'payments/home.html', context)

def charge(request):
    cart = Cart(request)
    cart.clear()
    return render(request, 'payments/charge.html')