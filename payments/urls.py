from django.urls import path

from . import views

app_name = 'payments'

urlpatterns = [
    # path('', views.HomePageView, name='home'),
    path('charge/', views.charge, name='charge'),
]