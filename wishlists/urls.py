from django.urls import path
from . import views



app_name = 'wishlists'

urlpatterns = [
    path('<int:product_id>/add/', views.add_wishlist , name='add_wishlist'),
    path('my_wishlists/', views.my_wishlists , name='my_wishlists'),
    path('clear_wishlists/', views.clear_wishlists , name='clear_wishlists'),
    path('<int:product_id>/delete_wishlist/', views.delete_wishlist , name='delete_wishlist'),
    # path('<int:post_id>/delete/', views.delete_wishlist , name='delete_wishlist'),


]
