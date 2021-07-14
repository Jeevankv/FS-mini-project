from django.urls import path
from . import views
urlpatterns = [
    path('', views.login, name= 'library-login'),
    path('register/', views.register, name = 'library-register'),
    path('adminlogin/', views.adminLogin, name = 'library-admin'),
    path('adminhome/', views.adminhome, name = 'library-adminhome'),
]
