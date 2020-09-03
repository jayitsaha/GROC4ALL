"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from ecommerce import views
from django.conf.urls import url

from django.conf.urls.static import static
from django.conf import settings
from polls.views import results
from personal.views import prediction

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('',views.initial),

    path('predict/',include('diseasepredictor.urls')),
    path('shop/',include('pages.urls')),
    path('cart/',include('cart.urls')),
    path('users/',include('users.urls')),
    path('wishlists/',include('wishlists.urls')),
    path('my-ajax-test/', views.myajaxtestview, name='myajaxtestview'),
    path('my-ajax-test-text/', views.myajaxtestviewtext, name='myajaxtestviewtext'),
    path('payments/', include('payments.urls')),
    path('search/' , views.search_titles ,name = 'search' ),
    path('updates/', include('processdata.urls')),
    path('updates/', include('app.urls')),  # add this
    path('updates/daily/',results,name='home'),
    # path('review/', include('personal.urls')),
    path('review/prediction/',prediction,name='predection')


]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

