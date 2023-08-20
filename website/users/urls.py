from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('employees/', views.employess, name='employees'),
    path('add_user/', views.add_user, name='add_user'),


]