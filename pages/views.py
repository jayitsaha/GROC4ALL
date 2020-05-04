from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
import random

from products.models import Product
from categories.models import Category


def home(request):
	#return HttpResponse('Hello')
	products = Product.objects.order_by('?')[:9]
	categories = Category.objects.all()
	context = {
		'title': 'Home',
		'categories': categories,
		'products' : products
	}
	return render(request,'ecom/index.html',context)


def about(request):
	context = {
		'title': 'About'
	}
	return render(request,'ecom/about.html',context)


def all_products(request):
	products = Product.objects.all()
	paginator = Paginator(products, 9)
	page = request.GET.get('page')
	products = paginator.get_page(page)
	context = {
		'title' : 'All Products',
		'products': products
	}
	return render(request,'ecom/all_products.html',context)


def product_by_slug(request,slug):
	product = Product.objects.get(slug=slug)
	if product.quantity >= 1:
		context = {
			'title' : product.title,
			'product': product
		}
		return render(request,'ecom/show.html',context)
	else:
		messages.warning(request,'Product is not Available')
		return redirect('pages:all_products')


def cart_add(request,slug):
	if len(request.session['cart']) == 0:
		return HttpResponse('ok')

def category_by_slug(request,slug):
	cat = Category.objects.get(slug=slug)
	products = Product.objects.filter(category=cat.id)
	paginator = Paginator(products, 3)
	page = request.GET.get('page')
	products = paginator.get_page(page)
	context = {
		'title' : 'All Products',
		'products': products
	}
	return render(request,'ecom/all_products.html',context)
