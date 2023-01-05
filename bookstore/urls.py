from django.urls import path     
from . import views


urlpatterns = [
    #path('', views.index),
    path('' , views.Home),
    path('Books/' , views.Books , name= "books"),
    path('create/' , views.create , name= "create"),
    path('customer/<str:pk>' , views.customer , name= "customer"),
    path('dashbord/' , views.dashbord , name="dashbord")	 ,
    path('update/<str:pk>' , views.Update , name="update")	 ,
    path('delete/<str:pk>' , views.delete , name="delete")	 ,
    path('regester/' , views.regester , name="regester")	 ,
    path('userlogin/' , views.userlogin , name="userlogin")	 ,
    path('logout/' , views.userlogout , name="logout")	 ,


]