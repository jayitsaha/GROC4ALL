from django.urls import path
from . import views



app_name = 'pages'

urlpatterns = [
    path('', views.home , name='home'),
    path('about/', views.about , name='about'),
    path('all_products/', views.all_products , name='all_products'),
    path('<slug:slug>/',views.product_by_slug , name='product_by_slug'),
    path('category/<slug:slug>/',views.category_by_slug , name='category_by_slug'),

]
