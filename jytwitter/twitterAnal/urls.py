from django.urls import path ,re_path
from . import views
app_name = "JY"
urlpatterns = [
    path('', views.main, name="main"),
    path(r'search/', views.search, name="search"),
    path(r'report/', views.report, name="report"),
    path('ajax/getData', views.getData, name='getData'), # ajax to send datas to client
    path('ajax/getSpecificDate', views.getData1, name='getData1')
]
