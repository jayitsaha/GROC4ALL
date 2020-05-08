from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib import messages
from django.conf import settings
from speechText.run import Run 

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