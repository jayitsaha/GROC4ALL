from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required

from products.models import Product
from categories.models import Category
from wishlists.models import WishList

@login_required(login_url="/users/login")
def add_wishlist(request,product_productid):
	product = get_object_or_404(Product,pk=product_productid)
	user_id = request.user.id
	wl = WishList(user_id=user_id,product=product)
	wl.save()
	if wl:
		messages.success(request,'WishLists Created SuccessFully')
		return redirect('/')
	else:
		messages.warning(request,'SomeThing Went Wrong')
		return redirect('/')

@login_required(login_url="/users/login")
def my_wishlists(request):
	products = WishList.objects.filter(user_id=request.user.id).select_related('product')
	wishlists = []
	for i in products:
		i = str(i)
		product = Product.objects.get(pk=i)
		wishlists.append(product)
	context = {
			'title' : 'My WishList',
			'wishlists' : wishlists
	}
	return render(request,'wishlists/all_wishlists.html',context)


@login_required(login_url="/users/login")
def clear_wishlists(request):
	products = WishList.objects.filter(user_id=request.user.id).select_related('product').delete()
	context = {
		'title' : 'My WishList',
	}
	return render(request,'wishlists/all_wishlists.html',context)

@login_required(login_url="/users/login")
def delete_wishlist(request,product_productid):
	wl = WishList.objects.get(product=product_productid)
	wl.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

