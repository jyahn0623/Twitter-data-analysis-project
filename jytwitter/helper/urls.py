from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('<room_num>/', views.room, name="room")
]
