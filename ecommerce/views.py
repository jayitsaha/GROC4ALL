from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib import messages
from django.conf import settings


def initial(request):
	context = {
		'title': 'About'
	}
	return render(request,'ecom/index_tobe.html',context)