from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from orders.models import Order
from products.models import Product
from users.models import User
from django.core.paginator import Paginator
from django.contrib import messages
from django.conf import settings
from speechText.run import Run
import json
from django.views.decorators.csrf import csrf_exempt
from chatbot1.shopping_bot import ShoppingBot

sb = ShoppingBot()
global x
def initial(request):
    # if(request.GET.get('mybtn')):
    #     x = Run.main()
    #     print(request)
    #     print("OH YEAH"+x)
    #     return redirect('/')
    context = {
		'title': 'About',
		# 'click':run(),
	}
    return render(request,'ecom/index_tobe.html',context)

def run():
    x = Run.main()

@csrf_exempt
def myajaxtestview(request):
    # print(x + "OH YEAH")
    # print('myajaxtestview')
    # if(request.POST['text']):
    x = Run.main()
    print(request)
    # print("OH YEAH"+x)
    s = request
    if(sb.temp > 0 or s == "checkout"):
        # print("Checking out")
        sb.temp = sb.temp + 1
        if(sb.temp == 1):
            # print("Showing list")
            resp = sb.handle("show list")
            resp,sb.other = resp
            resp = "Processing.... \nEnter your phone number:"
        elif(sb.temp == 2):
            sb.phone = int(s)
            resp = "Processing.... \nEnter your address:"
        else:
            sb.address = s
            for product,quantity in sb.other:
                p = Product.objects.get(slug=product)
                u = User.objects.get(username=request.user.username)
                o = Order(item=product,quantity=quantity,price=p.price,total=(int(quantity)*int(p.price)),name=request.user.username,phone=sb.phone,email=u.email,address=sb.address,user_id=u.id)
                o.save()
            resp = "Adding... \nCheck Dashboard" 
            sb.handle("clear list")    
            sb.temp = 0
             # print(other)
        data = json.dumps({
            'response': resp,
            'user': x,
        })
        return HttpResponse(data)

    resp = sb.handle(x)
    if(resp == None):
        # print("Added")
        resp = "Done..."
    else:
        print(resp)
    data = json.dumps({
        'response': resp,
        'user': x,
    })
        # return redirect('/')
    # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    # print(request.POST['text'])
    # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    # s = str(request.POST['text'])
    # resp = sb.handle(s)
    # # print("*********************************************************************")
    # if(resp == None):
    #     # print("Added")
    #     resp = "Done..."
    # else:
    #     print(resp)
    # print("*********************************************************************")
    return HttpResponse(data)


@csrf_exempt
def myajaxtestviewtext(request):
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(request.POST['text'])
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    s = str(request.POST['text'])

    if(sb.temp > 0 or s == "checkout"):
        # print("Checking out")
        sb.temp = sb.temp + 1
        if(sb.temp == 1):
            # print("Showing list")
            resp = sb.handle("show list")
            resp,sb.other = resp
            resp = "Processing.... \nEnter your phone number:"
        elif(sb.temp == 2):
            sb.phone = int(s)
            resp = "Processing.... \nEnter your address:"
        else:
            sb.address = s
            for product,quantity in sb.other:
                p = Product.objects.get(slug=product)
                u = User.objects.get(username=request.user.username)
                o = Order(item=product,quantity=quantity,price=p.price,total=(int(quantity)*int(p.price)),name=request.user.username,phone=sb.phone,email=u.email,address=sb.address,user_id=u.id)
                o.save()
            resp = "Adding... \nCheck Dashboard" 
            sb.handle("clear list")    
            sb.temp = 0
             # print(other)
        return HttpResponse(resp)

    resp = sb.handle(s)

    # print(resp)

    if type(resp) is tuple:
        resp,other = resp
        print(resp)

    # print("*********************************************************************")
    if(resp == "None"):
            resp = "Done..."
    else:
        print(resp)
    # print("*********************************************************************")
    return HttpResponse(resp)

def ordering():
    if(sb.temp == 1):
        resp = sb.handle("show list")
        resp,sb.other = resp
        resp = "Processing.... \nEnter your phone number:"
    elif(sb.temp == 2):
        sb.phone = int(s)
        resp = "Processing.... \nEnter your address:"
    else:
        sb.address = s
        for product,quantity in sb.other:
            p = Product.objects.get(slug=product)
            u = User.objects.get(username=request.user.username)
            o = Order(item=product,quantity=quantity,price=p.price,total=(int(quantity)*int(p.price)),name=request.user.username,phone=sb.phone,email=u.email,address=sb.address,user_id=u.id)
            o.save()
        resp = "Adding... \nCheck Dashboard" 
        sb.handle("clear list")    
        sb.temp = 0
    # print(other)
    return HttpResponse(resp)




