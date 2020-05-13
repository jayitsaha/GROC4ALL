from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
import random
from django.db.models import Count

from products.models import Product
from categories.models import Category


def home(request):
	#return HttpResponse('Hello')
	# products = Product.objects.order_by('?')[:9]
	products = Product.objects.values('title').annotate(pcount=Count('title'))
	print(products)
	prdct=[]
	for prod in products:
		prods = Product.objects.filter(
			title=prod['title']
		)[0]
		prdct.append(prods)
	categories = Category.objects.all()
	print(categories)
	context = {
		'title': 'Home',
		'categories': categories,
		'products' : prdct
	}
	return render(request,'ecom/index.html',context)


def about(request):
	context = {
		'title': 'About'
	}
	return render(request,'ecom/about.html',context)


def all_products(request):
	products = Product.objects.values('title').annotate(pcount=Count('title'))
	print(products)
	paginator = Paginator(products, 9)
	page = request.GET.get('page')
	products = paginator.get_page(page)
	categoriess = Category.objects.all()

	context = {
		'title' : 'All Products',
		'products': products,
		'categories': categoriess,

	}
	return render(request,'ecom/all_products.html',context)


def product_by_slug(request,product_productid):
	product = Product.objects.get(productid=product_productid)
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

def prod_detail(request,title):
	products = Product.objects.filter(
		title = title
	)

	context = {
		'title': products[0].title,
		'image': products[0].photo.url,
		'products': products,
	}

	return render(request,'ecom/prod_detail.html', context)

