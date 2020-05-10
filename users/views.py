# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import users.face_detect as face_detect
from users.models import Profile
from orders.models import Order
from django.conf import settings
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
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

def register(request):
	if request.user.is_authenticated == False:
		if request.method == 'POST':
			username = request.POST['username']
			email = request.POST['email']
			password = request.POST['password']
			password2 = request.POST['password2']
			img_encoded = request.POST['mydata']
			img_decode = base64.b64decode(img_encoded)
					
			
			if password == password2:
				if User.objects.filter(username=username).exists():
						messages.error(request , 'User Name Already Taken')
						return redirect('users:register')
				else:
					if User.objects.filter(email=email).exists():
						messages.error(request , 'Email Already Exits ')
						return redirect('users:register')
					else:
						user = User.objects.create_user(username=username,password=password,email=email)
						
						Profile.objects.update_or_create(
							user=user,
							
						)
						user.save()
						profile = Profile.objects.get(user=user)
						profile.image = ContentFile(img_decode, 'profile.jpg')
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


def login(request):
	if request.user.is_authenticated == False:
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']

			user = auth.authenticate(username=username , password=password)
			if user is not None:
				res = face_detect.check(user)
				if res:
					auth.login(request,user)
					messages.success(request,'You Are Now LoggedIn')
					return redirect('users:dashboard')
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
def dashboard(request):
	orders = Order.objects.filter(user_id=request.user.id)
	context = {
		'title': request.user.username + ' Shopping Details',
		'orders': orders
	}
	return render(request,'users/dashboard.html',context)

@login_required(login_url="/users/login")
def profile(request,user_id):
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
def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		messages.success(request,'You Are Now Logged Out')
		return redirect('pages:home')

# class SaveImage(TemplateView):

# 	@csrf_exempt
# 	def dispatch(self, *args, **kwargs):
# 		self.filename = self.kwargs['cedula']+'.jpg'
# 		return super(SaveImage, self).dispatch(*args, **kwargs)

# 	def post(self, request, *args, **kwargs):
		
# 		# save it somewhere
# 		f = open(settings.MEDIA_ROOT + '/webcamimages/'+ self.filename, 'wb')
# 		f.write(request.body)
# 		f.close()
# 		# return the URL
# 		return HttpResponse("/media/webcamimages/" + self.filename)

# 	def get(self, request, *args, **kwargs):
# 		return HttpResponse('No esta pasando el POST')