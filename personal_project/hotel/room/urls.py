from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_dashboard, name='customer_dashboard'),
    path('roomList/', views.roomList, name='room_list'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]