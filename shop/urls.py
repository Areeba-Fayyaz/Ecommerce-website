from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path ("", views.index, name = 'MyShop'),
    path ("", views.singleProductPage, name = 'singleProductPage'),
    path ("search/", views.search, name = 'search'),
    path ("", views.confirmReturn, name = 'confirmReturn'),
    path ("", views.refundRequest, name = 'refundRequest'),
    path ("", views.cart, name = 'cart'),
    path ("", views.signinup, name = 'signinup'),
    path ("", views.signin, name = 'signin'),
    path ("", views.signup, name = 'signup'),
    path ("", views.checkout, name = 'checkout'),
    path ("", views.orderSuccess, name = 'orderSuccess')

]
