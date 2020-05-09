from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib import messages
from django.conf import settings
from speechText.run import Run
import json
from django.views.decorators.csrf import csrf_exempt
from chatbot.shopping_bot import ShoppingBot

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
    # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    # print(request.POST['text'])
    # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    s = str(request.POST['text'])
    resp = sb.handle(s)
    # print("*********************************************************************")
    if(resp == None):
        # print("Added")
        resp = "Done..."
    else:
        print(resp)
    # print("*********************************************************************")
    return HttpResponse(resp)




