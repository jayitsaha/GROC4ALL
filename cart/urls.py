from django.urls import path
from . import views



app_name = 'cart'

urlpatterns = [
    path('add/<slug:slug>/',views.cart_add , name='cart_add'),
    path('cart_detail',views.cart_detail , name='cart_detail'),
    path('item_clear/<slug:slug>/',views.item_clear , name='item_clear'),
    path('item_increment/<slug:slug>/',views.item_increment , name='item_increment'),
    path('item_decrement/<slug:slug>/',views.item_decrement , name='item_decrement'),
    path('checkout/',views.checkout,name='checkout'),
    path('cart_clear/',views.cart_clear , name='cart_clear'),
	path('confrm_checkout/',views.confrm_checkout , name='confrm_checkout'),
]
