from django.urls import path
from . import views
from ecommerce.views import search_titles ,myajaxtestview,myajaxtestviewtext


app_name = 'pages'

urlpatterns = [
    path('', views.home , name='home'),
    path('prod_detail/<str:title>',views.prod_detail, name='prod_detail'),
    path('about/', views.about , name='about'),
    path('all_products/', views.all_products , name='all_products'),
    path('<int:product_productid>/',views.product_by_slug , name='product_by_slug'),
    path('category/<slug:slug>/',views.category_by_slug , name='category_by_slug'),
    path('search/' , search_titles ,name = 'search' ),
    path('my-ajax-test/', myajaxtestview, name='myajaxtestview'),
    path('my-ajax-test-text/', myajaxtestviewtext, name='myajaxtestviewtext'),




]
