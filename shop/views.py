from django.shortcuts import render
from django.http import HttpResponse
from .models import Item, Delivery, Payment, Buyer, Seller


def index(request):
    product=Item.objects.all()
    noOfProducts=len(product)
    params={'product':product, 'range': range (noOfProducts)}
    return render (request,'index.html',params)

def singleProductPage(request):
    return HttpResponse("singleProductPage")

def searchMatch(query,item):
     if query!="":
        Query=query[0].upper()+query[1:]  
        if query in str(item.productName ).lower() or  query in str(item.productType).lower() or query in str(item.description).lower() \
        or query in str(item.productName ).upper() or  query in str(item.productType).upper() or query in str(item.description).upper()\
            or Query in str(item.productName ) or  Query in str(item.productType) or Query in str(item.description):
            return True
        else:
            return False

def search(request):
    query=request.GET.get('search')
    prod=Item.objects.all()
    #print (prod)
    msg=''
    product=[item for item in prod if searchMatch(query,item) ]
    #print(product)
    noOfProducts=len(product)
    if noOfProducts==0 or query=="":
        product=Item.objects.all()
        msg='Please make sure to enter relevant search query'
    params={'product':product, 'range': range (noOfProducts),'msg':msg}

    return render (request,'search.html',params)


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