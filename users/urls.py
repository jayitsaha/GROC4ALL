from django.urls import path
from . import views



app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout , name='logout'),
    path('dashboard/', views.dashboard , name='dashboard'),
    path('<int:user_id>/profile/', views.profile , name='profile'),
    # path('myposts/', views.myposts , name='myposts'),
]
