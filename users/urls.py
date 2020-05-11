from django.urls import path
from . import views
from users.views import SellerSignUpView



app_name = 'users'

urlpatterns = [
    path('login/', views.login_customer, name='login'),
    path('register/', views.register_customer, name='register'),
    path('logout/', views.logout_customer , name='logout'),
    path('dashboard/', views.dashboard_customer , name='dashboard'),
    path('seller/',views.seller_product , name='home'),
    path('<int:user_id>/profile/', views.profile_customer , name='profile'),
    path('accounts/signup/teacher/', SellerSignUpView.as_view(), name='teacher_signup'),
    # path('accounts/signup/student/', StudentSignUpView.as_view(), name='student_signup'),
    path('seller/add',views.seller_product_add , name='add'),

    # path('myposts/', views.myposts , name='myposts'),
]
