from django.urls import path
from . import views
urlpatterns = [
    path('', views.login, name= 'library-login'),
    path('register/', views.register, name = 'library-register'),
    path('adminlogin/', views.adminLogin, name = 'library-admin'),
    path('adminhome/', views.adminhome, name = 'library-adminhome'),
    path('libraryhome/', views.libraryhome, name = 'library-home'),
    path('addbooks/', views.addbooks, name = 'library-addbooks'),
    path('deletebooks/', views.deletebooks, name = 'library-deletebooks'),
    path('displaybooks/', views.displaybooks, name = 'library-displaybooks'),
    path('login/', views.reopen_login, name = 'library-reopenlogin'),
    path('borrow/', views.borrowbook, name = 'library-borrowbook'),
    path('return/', views.returnbook, name = 'library-returnbook'),
    path('searchResult/', views.search, name = 'library-searchResult'),
]
