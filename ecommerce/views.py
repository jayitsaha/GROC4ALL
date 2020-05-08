from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib import messages
from django.conf import settings
from speechText.run import Run 

from django.views.decorators.csrf import csrf_exempt
from chatbot.shopping_bot import ShoppingBot

sb = ShoppingBot()

def initial(request):
	if(request.GET.get('mybtn')):
		Run.main()
		print(request)
		return redirect('/')

		

	context = {
		'title': 'About',
		# 'click':run(),
	}
	return render(request,'ecom/index_tobe.html',context)

def run():
	Run.main()

@csrf_exempt
def myajaxtestview(request):
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