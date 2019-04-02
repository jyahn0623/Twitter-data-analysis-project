from django.urls import path
from . import views
app_name = "JY"
urlpatterns = [
    path('', views.main, name="main"),
    path('ajax/getData', views.getData, name='getData')
]
