from django.urls import include,path
from . import views


app_name='polls'

urlpatterns=[
    path('<int:question_id>/results/', views.results, name='results'),
    path('resultsdata/<str:obj>/', views.resultsData, name="resultsdata"),
]
