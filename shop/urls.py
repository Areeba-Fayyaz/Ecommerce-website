from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path ("", views.index, name = 'MyShop'),
    path ("productpage/<int:id>", views.singleProductPage, name = 'singleProductPage'),
    path ("search/", views.search, name = 'search'),
    path ("", views.confirmReturn, name = 'confirmReturn'),
    path ("refundRequest/", views.refundRequest, name = 'refundRequest'),
    path ("", views.cart, name = 'cart'),
    path ("", views.signinup, name = 'signinup'),
    path ("", views.signin, name = 'signin'),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path ("", views.checkout, name = 'checkout'),
    path ("ordersuccess/", views.orderSuccess, name = 'orderSuccess')

]
