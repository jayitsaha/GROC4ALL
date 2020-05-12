from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages,auth
from django.views.decorators.http import require_POST
from .cart import Cart
from orders.models import Order

@login_required(login_url="/users/login")
def cart_add(request, product_productid):
	cart = Cart(request)
	product = Product.objects.get(productid=product_productid)
	cart.add(product=product)
	return redirect('/shop/')

@login_required(login_url="/users/login")
def cart_detail(request):
	sub = []
	qty = []
	total = 0
	for key,value in request.session['cart'].items():
		sub.append(float(value['price']) * float(value['quantity']))
		qty.append(int(value['quantity']))
	for s in sub:
		total = total + s
	context = {
    	'title' : 'My Cart',
    	'sub' : sub,
    	'total' : total
    }
	return render(request,'cart/cart_detail.html',context)

@login_required(login_url="/users/login")
def item_clear(request,product_productid):
	cart = Cart(request)
	product = Product.objects.get(productid=product_productid)
	cart.remove(product)
	return redirect('cart:cart_detail')

@login_required(login_url="/users/login")
def item_increment(request,product_productid):
	cart = Cart(request)
	product = Product.objects.get(productid=product_productid)
	cart.add(product=product)
	return redirect('cart:cart_detail')

@login_required(login_url="/users/login")
def item_decrement(request,product_productid):
	cart = Cart(request)
	product = Product.objects.get(productid=product_productid)
	cart.decrement(product=product)
	return redirect('cart:cart_detail')

@login_required(login_url="/users/login")
def cart_clear(request):
	cart = Cart(request)
	cart.clear()
	return redirect('cart:cart_detail')

@login_required(login_url="/users/login")
def checkout(request):
	sub = []
	qty = []
	total = 0
	if len(request.session['cart']) != 0:
		for key,value in request.session['cart'].items():
			sub.append(float(value['price']) * float(value['quantity']))
			qty.append(int(value['quantity']))
		for s in sub:
			total = total + s
		context = {
	    	'title' : 'CheckOut',
	    	'sub' : sub,
	    	'total' : total
	    }
		return render(request,'cart/checkout.html',context)
	else:
		messages.info(request,"Your cart Is Empty")
		return redirect('/')

@login_required(login_url="/users/login")
def confrm_checkout(request):
	if len(request.session['cart']) != 0:
		if request.method == 'POST':
			name = request.POST['name']
			phone = request.POST['phonenumber']
			email = request.POST['email']
			address = request.POST['address']
			user_id = request.user.id
			if name and phone and email and address:
				for key,value in request.session['cart'].items():
					item = value['title']
					product_id = value['productid']
					product_object = Product.objects.filter(productid = product_id)[0]
					quantity = value['quantity']
					price = value['price']
					total = (float(quantity) * float(price))
					order = Order(item=item,productid=product_object , quantity=quantity,price=price,total=total,name=name,phone=phone,email=email,address=address,user_id=user_id)
					order.save()
				cart_clear(request)
				messages.success(request,'Order Created SuccessFully')
				return redirect('users:dashboard')
			else:
				messages.info(request,'Filled All The Field')
				return redirect('cart:checkout')
		else:
			messages.warning(request,'SomeThing Went Wrong')
			return redirect('cart:checkout')
	else:
		messages.info(request,"Your cart Is Empty")
		return redirect('/')


