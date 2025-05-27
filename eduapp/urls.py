from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.students_table, name='students_table'),
    path('add/', views.add_student, name='add_student'),
    path('filter/', views.filter_students, name='filter_students'),
]
