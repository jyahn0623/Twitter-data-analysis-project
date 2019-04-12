from . import views
from django.urls import path
from django.conf import settings

app_name = 'csvdata'
urlpatterns = [
    path('', views.datamain, name='datamain'),
]
