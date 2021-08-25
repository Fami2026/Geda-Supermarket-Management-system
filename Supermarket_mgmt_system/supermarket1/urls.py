
from django.urls import path
from . import views 
from .views import *




urlpatterns = [
    path('', views.home,name="home"),
    path("home1/", HomeView.as_view(), name="home"),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
     path('user/', views.userPage, name="user-page"),

    path('register/', views.registerpage, name="register"),
     path('customer/<str:pk_test>/', views.customer,name='customer-page'),
     path('product/', views.product, name='product-page'),
     path('create_order/<str:pk>', views.createOrder, name='create_order'),
     path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),

    path('about/', views.AboutView.as_view(), name="view"),
   path('contact/', views.ContactView.as_view(), name="contact"),
   path('advertise/', views.AdvertiseView.as_view(), name="advertise"),
    path('footer/', views.Footer.as_view(), name="footer"),



    ]
