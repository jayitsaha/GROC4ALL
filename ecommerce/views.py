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
# from chatbot1.shopping_bot import ShoppingBot
from cart.cart import Cart
# from django.shortcuts import render_to_response

# sb = ShoppingBot()
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

def convert(s):



    dict_trivial = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8","nine":"9", "ten":"10"}
    dict_teen = {"eleven":"11", "twelve":"12", "thirteen":"13", "fourteen":"14", "fifteen":"15","sixteen":"16", "seventeen":"17", "eighteen":"18", "nineteen":"19"}

    dict_large = {"twenty one":"21", "twenty two":"22", "twenty three":"23", "twenty four":"24", "twenty five":"25", "twenty six":"26","twenty seven":"27", "twenty eight":"28", "twenty nine":"29","twenty":"20",
    "thirty one":"31", "thirty two":"32", "thirty three":"33", "thirty four":"34", "thirty five":"35", "thirty six":"36","thirty seven":"37", "thirty eight":"38", "thirty nine":"39","thirty":"30",
    "fourty one":"41", "fourty two":"42", "fourty three":"43", "fourty four":"44", "fourty five":"45", "fourty six":"46","fourty seven":"47", "fourty eight":"48", "fourty nine":"49","fourty":"40",
    "fifty one":"51", "fifty two":"52", "fifty three":"53", "fifty four":"54", "fifty five":"55", "fifty six":"56","fifty seven":"57", "fifty eight":"58", "fifty nine":"59","fifty":"50",
    "sixty one":"61", "sixty two":"62", "sixty three":"63", "sixty four":"64", "sixty five":"65", "sixty six":"66","sixty seven":"67", "sixty eight":"68", "sixty nine":"69","sixty":"60",
    "seventy one":"71", "seventy two":"72", "seventy three":"73", "seventy four":"74", "seventy five":"75", "seventy six":"76","seventy seven":"77", "seventy eight":"78", "seventy nine":"79","seventy":"70",
    "eighty one":"81", "eighty two":"82", "eighty three":"83", "eighty four":"84", "eighty five":"85", "eighty six":"86","eighty seven":"87", "eighty eight":"88", "eighty nine":"89","eighty":"80",
    "ninety one":"91", "ninety two":"92", "ninety three":"93", "ninety four":"94", "ninety five":"95", "ninety six":"96","ninety seven":"97", "ninety eight":"98", "ninety nine":"99","ninety":"90",
    }

    list = {"twenty":"1" , "thirty":"1" , "fourty":"1" , "fifty":"1","sixty":"1","seventy":"1","eighty":"1","ninety":"1"}
    flag = 0
    for i in list:
        print(i)
        x = s.find(i)
        print(x)
        if(s.find(i)>=0):
            print(i)
            for k in dict_large:
                if(s.find(k)):
                    s = s.replace(k,dict_large[k])
                    flag = 1

    print("FLAg")

    print(flag)
    flag1 = 0
    if(flag==0):
            # print("HIII")
        for j in dict_teen:
            if(s.find(j)>=0):
                s = s.replace(j,dict_teen[j])
                print(j)

                flag1 = 1
    print("FLAG 1")
    print(flag1)
    if(flag1==0):
            # print("HIII")
        for x in dict_trivial:
            if(s.find(x)):
                s = s.replace(x,dict_trivial[x])



    return s
# @csrf_exempt
# def myajaxtestview(request):
#     # print(x + "OH YEAH")
#     # print('myajaxtestview')
#     # if(request.POST['text']):
#     # dict = {"one":"1" , "two":"2"}
#     x = Run.main()
#     x = convert(x)
#     print(x)

#     print(request)
#     # print("OH YEAH"+x)
#     s = request
#     if(sb.temp > 0 or s == "checkout"):
#         # print("Checking out")
#         sb.temp = sb.temp + 1
#         if(sb.temp == 1):
#             # print("Showing list")
#             resp = sb.handle("show list")
#             resp,sb.other = resp
#             resp = "Processing.... \nEnter your phone number:"
#         elif(sb.temp == 2):
#             sb.phone = int(s)
#             resp = "Processing.... \nEnter your address:"
#         else:
#             sb.address = s
#             for product,quantity in sb.other:
#                 p = Product.objects.get(slug=product)
#                 u = User.objects.get(username=request.user.username)
#                 o = Order(item=product,quantity=quantity,price=p.price,total=(int(quantity)*int(p.price)),name=request.user.username,phone=sb.phone,email=u.email,address=sb.address,user_id=u.id)
#                 o.save()
#             resp = "Adding... \nCheck Dashboard"
#             sb.handle("clear list")
#             sb.temp = 0
#              # print(other)
#         data = json.dumps({
#             'response': resp,
#             'user': x,
#         })
#         return HttpResponse(data)

#     resp = sb.handle(x)
#     if(resp == None):
#         # print("Added")
#         resp = "Done..."
#     else:
#         print(resp)
#     data = json.dumps({
#         'response': resp,
#         'user': x,
#     })
#         # return redirect('/')
#     # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
#     # print(request.POST['text'])
#     # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
#     # s = str(request.POST['text'])
#     # resp = sb.handle(s)
#     # # print("*********************************************************************")
#     # if(resp == None):
#     #     # print("Added")
#     #     resp = "Done..."
#     # else:
#     #     print(resp)
#     # print("*********************************************************************")
#     return HttpResponse(data)

@csrf_exempt
def myajaxtestview(request):
    # print(x + "OH YEAH")
    # print('myajaxtestview')
    # if(request.POST['text']):
    # dict = {"one":"1" , "two":"2"}
    print("hii")
    x = Run.main()
    x = convert(x)
    print(x)

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

            sb.address = s
            for product,quantity in sb.other:
                print("YO")
                p1 = Product.objects.filter(slug = product)[0]
                p = Product.objects.get(productid=p1.productid)

                cart = Cart(request)

                cart.add(product = p , quantity = quantity)
            resp = "Adding... \nCheck CART"
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
    # # print("***********************")
    # if(resp == None):
    #     # print("Added")
    #     resp = "Done..."
    # else:
    #     print(resp)
    # print("***********************")
    return HttpResponse(data)


@csrf_exempt
def myajaxtestviewtext(request):
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(request.POST['text'])
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    s = str(request.POST['text'])
    sb.temp = 0
    if(sb.temp > 0 or s == "checkout"):
        # print("Checking out")
        sb.temp = sb.temp + 1
        if(sb.temp == 1):
            resp = sb.handle("show list")
            resp , sb.other = resp

            sb.address = s
            flag=0
            for product,quantity in sb.other:
                print("YO")
                p1 = Product.objects.filter(slug = product)[0]
                p = Product.objects.get(productid=p1.productid)
                cart = Cart(request)
                qty = p.quantity
                if quantity>qty:
                    resp = "Number of Items exceeded the stock..\nPlease Clear the list and try again."
                    return HttpResponse(resp)
                p.quantity = qty-quantity
                p.save()
                cart.add(product = p , quantity = quantity)
                # u = User.objects.get(username=request.user.username)
                # o = Order(item=product,quantity=quantity,price=p.price,total=(int(quantity)*int(p.price)),name=request.user.username,phone=sb.phone,email=u.email,address=sb.address,user_id=u.id)
                # o.save()
            resp = "Adding... \nCheck CART"
            sb.handle("clear list")
            sb.temp = 0
             # print(other)
        return HttpResponse(resp)
    if(s == "clear cart" or s=="empty cart"):
        cart = Cart(request)
        cart.clear()
        resp = "CLEARING CART"

             # print(other)
        return HttpResponse(resp)
    resp = sb.handle(s)

    # print(resp)

    if type(resp) is tuple:
        resp,other = resp
        print(resp)

    # print("***********************")
    if(resp == "None"):
            resp = "Done..."
    else:
        print(resp)
    # print("***********************")
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

@csrf_exempt
def search_titles(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''
    articles = Product.objects.filter(title__contains = search_text , title__isnull = False)




    return render(None,'ecom/search.html',{"articles":articles})




