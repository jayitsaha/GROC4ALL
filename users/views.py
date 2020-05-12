# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages,auth
# from django.contrib.auth.models import User
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError
from django.core.paginator import Paginator
from django.contrib.auth import login
# from decorators import customer_required
from django.contrib.auth.decorators import login_required
import users.face_detect as face_detect
from users.models import Profile,User
from orders.models import Order
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from categories.models import Category
from django.shortcuts import get_object_or_404, redirect, render
from users.forms import SellerSignUpForm
import base64
from PIL import Image
from io import BytesIO
import cv2
import numpy as np
from django.core.files import File
from django.core.files.base import ContentFile
import requests
import os
from urllib.parse import urlparse
def register_customer(request):
	if request.user.is_authenticated == False:
		if request.method == 'POST':
			username = request.POST['username']
			email = request.POST['email']
			password = request.POST['password']
			password2 = request.POST['password2']
			# img_encoded = request.POST['mydata']
			# img_decode = base64.b64decode(img_encoded)


			if password == password2:
				if User.objects.filter(username=username).exists():
						messages.error(request , 'User Name Already Taken')
						return redirect('users:register')
				else:
					if User.objects.filter(email=email).exists():
						messages.error(request , 'Email Already Exits ')
						return redirect('users:register')
					else:
						user = User.objects.create_user(username=username,password=password,email=email,is_customer=True)

						Profile.objects.update_or_create(
							user=user,

						)
						user.save()
						profile = Profile.objects.get(user=user)
						# profile.image = ContentFile(img_decode, 'profile.jpg')
						profile.save()
						messages.success(request,'You Are Now Registered')
						return redirect('users:login')
			else:
				messages.error(request , 'Password Doest Not Match')
				return redirect('users:register')

		else:
			return render(request,'users/register.html')
	else:
		messages.info(request , 'You Are Already Logged In')
		return redirect('users:dashboard')

def login_customer(request):
	if request.user.is_authenticated == False:
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']

			user = auth.authenticate(username=username , password=password)

			if(User.objects.filter(username = username)):
				if(User.objects.filter(username = username).values("is_customer")):
					if(User.objects.filter(username = username).values("is_customer")[0]):
						is_customer = User.objects.filter(username = username).values("is_customer")[0]["is_customer"]
			if(User.objects.filter(username = username)):
				if(User.objects.filter(username = username).values("is_seller")):
					if(User.objects.filter(username = username).values("is_seller")[0]):
						is_seller = User.objects.filter(username = username).values("is_seller")[0]["is_seller"]
			# is_seller = User.objects.filter(username = username).values("is_seller")[0]["is_seller"]

			if user is not None and is_customer:
				# res = face_detect.check(user)
				print("CUSTOMER PRINTING")
				res = True
				if res:
					auth.login(request,user)
					messages.success(request,'You Are Now LoggedIn')
					return redirect('users:dashboard')
				messages.error(request,'Unauthorized access')
				return render(request,'users/login.html')


			elif user is not None and is_seller:
				# res = face_detect.check(user)
				res = True
				if res:
					print("SELLER PRINTING")
					auth.login(request,user)
					messages.success(request,'You Are Now LoggedIn')
					return redirect('users:home')
				messages.error(request,'Unauthorized access')
				return render(request,'users/login.html')
			else:
				messages.error(request,'Invalid Credentials')
				return redirect('users:login')

		else:
			return render(request,'users/login.html')

	else:
		messages.error(request,'You Are Alredy Logged In')
		return redirect('users:dashboard')



@login_required(login_url="/users/login")
def dashboard_customer(request):
	print("DASHBOARD PRINTING")
	orders = Order.objects.filter(user_id=request.user.id)
	print(orders)
	context = {
		'title': request.user.username + ' Shopping Details',
		'orders': orders
	}
	return render(request,'users/dashboard.html',context)

def dashboard_seller(request):
	order_seller = []
	for i in range(100):
		if(Order.objects.filter(productid = i)):
			if(Product.objects.filter(productid =i).values()[0]['user_id'] == request.user.id):
				print("HIIII")
				order = Order.objects.filter(productid = i).values()
				print(order)
				order_seller.append(order)
				x = order_seller[0]
				print(x[0])
				print(x)
				context={

					'order':order_seller,
					'jayit':x,
				}
	return render(request,'seller/sellerorder.html',context)
		# 	else:
		# 		return redirect('users:home')
		# else:
		# 	return redirect('users:home')

	# if(None):
	# 	return redirect('users:home')

	# product_object = Product.objects.filter(productid ="1").values()[0]['user_id']


@login_required(login_url="/users/login")
def profile_customer(request,user_id):
	if request.method == 'POST':
		try:
			image = request.FILES['image']
		except MultiValueDictKeyError:
			image = False
		username = request.POST['username']
		email = request.POST['email']
		user = get_object_or_404(User,pk=user_id)
		profile = Profile.objects.get(user=user_id)
		if image == False:
			user.username = username
			user.email = email
			user.save()
			messages.success(request,'Profile Updated SuccessFully')
			return redirect('users:profile',user_id = user_id)
		else:
			user.username = username
			user.email = email
			profile.image = image

			user.save()
			profile.save()
			messages.success(request,'Profile Updated SuccessFully')
			return redirect('users:profile',user_id = user_id)
	else:
		return render(request,'users/profile.html')

@login_required(login_url="/users/login")
def logout_customer(request):
	if request.method == 'POST':
		auth.logout(request)
		messages.success(request,'You Are Now Logged Out')
		return redirect('pages:home')

class SellerSignUpView(CreateView):
    model = User
    form_class = SellerSignUpForm
    template_name = 'seller/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Seller'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/shop')


# class StudentSignUpView(CreateView):
#     model = User
#     form_class = StudentSignUpForm
#     template_name = 'registration/signup_form.html'

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'student'
#         return super().get_context_data(**kwargs)

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('/shop')


def seller_product(request):
	if(request.user):
		if(request.user.is_seller):
			user_id = request.user.id

			products = Product.objects.filter(user =user_id)
			print(products)
			context = {

				# 'title':request.user.name,
				'products':products
			}
			return render(request ,'seller/home.html' , context)
		else:
			return render(request,'users/login.html')

def seller_product_add(request):
	if(request.user):
		if(request.user.is_seller):
			user_id = request.user.id
			categories = Category.objects.all()
			# categories1 = categories[0]

			if request.method == 'POST':
				try:
					image = request.FILES['image']
				except MultiValueDictKeyError:
					image = False
				title = request.POST['title']
				price = request.POST['price']
				description = request.POST['description']
				quantity = request.POST['quantity']
				category = request.POST['category']
				category1 = Category.objects.filter(title=category)[0]
				# quantity = request.POST['quantity']
				# published_at = request.POST['date']
				# print(prod)

				if True:
					prod = Product.objects.create(user=request.user , title = title ,slug = title , price = price , quantity = quantity , description=description , photo = image , category = category1 )
					# prod.id
					print(prod)
					# prod.user = user_id
					# prod.title = title
					# prod.slug = title
					# prod.price = price
					# prod.quantity = quantity
					# prod.description = description
					# prod.photo = image
					# prod.category = category
					# # Product.published_at = published_at
					prod.save()
					print("WOOPS")
					print(prod)
					messages.success(request , 'PRODUCT ADDED')
					return redirect('users:home')
			# products = Product.objects.filter(user =user_id)
			# print(products)
			context = {
				'category':categories,
				# 'title':request.user.name,
				# 'products':"products"
			}
			return render(request ,'seller/add.html' , context)
		else:
			return render(request,'users/login.html')

# def seller_product_add(request):
# 	form = ProductAddForm()
# 	if request.method =='POST':
# 		form = ProductAddForm(request.POST)
# 		if form.is_valid():
# 			form_hold = form.save(commit=False)
# 			form_hold.user = request.user.id
# 			form_hold.save()
# 			return redirect('users:home')
# 	context = {
#         'form': form
#     }
# 	return render(request , 'seller/add' , context)