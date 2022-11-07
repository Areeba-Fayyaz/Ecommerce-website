from django.shortcuts import render
from django.http import HttpResponse
from .models import Item, Delivery, Payment, Buyer, Seller

def index(request):
    product=Item.objects.all()
    print(product)
    noOfProducts=len(product)
    params={'product':product, 'range': range (noOfProducts)}
    return render (request,'index.html',params)

def singleProductPage(request):
    return HttpResponse("singleProductPage")

def search(request):
    return HttpResponse("search")

def confirmReturn(request):
    return HttpResponse("confirmReturn")

def refundRequest(request):
    return HttpResponse("My shop")

def signinup(request):
    return HttpResponse("signinup")

def signin(request):
    return HttpResponse("My shop")

def signup(request):
    return HttpResponse("My shop")

def cart(request):
    return HttpResponse("My shop")

def checkout(request):
    return HttpResponse("My shop")

def orderSuccess(request):
    return HttpResponse("My shop")