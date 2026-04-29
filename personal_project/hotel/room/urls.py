from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('roomList/', views.roomList, name='room_list'),
]