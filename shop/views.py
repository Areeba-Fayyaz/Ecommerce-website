from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages 
from django.contrib.auth.models import User 
from .models import Item
# , Delivery, Payment, Buyer, Seller


def index(request):
    product=Item.objects.all()
    noOfProducts=len(product)
    params={'product':product, 'range': range (noOfProducts)}
    return render (request,'index.html',params)

def singleProductPage(request, id):
    product=Item.objects.filter(id=id)
    print(product)
    return  render (request,'productpage.html', {'product':product[0]})

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
     return render (request,'refundRequest.html')

def signinup(request):
    return HttpResponse("signinup")

def signin(request):
    return HttpResponse("My shop")

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.name= fname+lname
        myuser.email= email
        myuser.username= username
        myuser.password= pass1
        myuser.save()
        messages.success(request, " Your account has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")

def signup(request):
    return HttpResponse("My shop")

def cart(request):
    return HttpResponse("My shop")

def checkout(request):
    return HttpResponse("My shop")

def orderSuccess(request):
    return render (request,'orderPlaced.html')