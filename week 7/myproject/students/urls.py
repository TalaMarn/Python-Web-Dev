from django.urls import path
from . import views

urlpatterns = [
    # path('', views.student_list, name='student_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.welcome, name='welcome'),
    path('add/', views.add_student, name='add_student'),
    path('students/', views.student_list, name='student_list'),
    path('edit_student/<int:id>/', views.edit_student, name='edit_student'),
    path('delete_student/<int:id>/', views.delete_student, name='delete_student'),
]