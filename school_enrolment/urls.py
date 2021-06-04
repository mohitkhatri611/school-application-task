"""school URL Configuration
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.add_student, name="add_student"),
    path('display_student/<id>/', views.display_student, name="display_student"),
    path('edit_student/<id>/', views.edit_student, name="edit_student"),
    path('check_email_exist/', views.check_email_exist, name="check_email_exist"),
    path('check_phone_exist/', views.check_username_exist, name="check_phone_exist"),

]
