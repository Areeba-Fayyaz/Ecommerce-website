from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout
from .models import Item,Buyer
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

def handleLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(request, username= loginusername, password= loginpassword)
        print(user)
        print(user is not None)
        if user is not None:
            login(request, user)
            print(loginusername)
            print(loginpassword)
            messages.success(request, "Successfully Logged In")
            return redirect("MyShop")
        else:
            print(loginusername,'===================')
            print(loginpassword)
            messages.warning(request, "Invalid credentials! Please try again")
            return redirect("MyShop")

    return HttpResponse("404- Not found")

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('MyShop')


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
        # if len(username)<10:
        #     messages.warning(request, " Your user name must be greator than 10 characters")
            # '{{% block body %}} <div class="alert alert-danger" role="alert">A simple danger alert—check it out!</div>{{% endblock %}}'
            # return redirect('MyShop')

        if not username.isalnum():
            messages.warning(request, " User name should only contain letters and numbers")
            return redirect('MyShop')
        if (pass1!= pass2):
             messages.warning(request, " Passwords do not match")
             return redirect('MyShop')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name=lname
        myuser.email= email
        myuser.username= username
        myuser.set_password(pass1)
        myuser.save()
        messages.success(request, " Your account has been successfully created")
        return redirect('/')

    else:
        return HttpResponse("404 - Not found")

def signup(request):
    return HttpResponse("My shop")

def cart(request):
    return HttpResponse("My shop")


def checkout(request):
    product=Item.objects.all()
    print( request.method)
    if request.method=="POST":
        itemsJson=request.POST.get('itemsJson', '')
        name = request.POST.get('firstName', '')+' '+ request.POST.get('lastName', '')
        print(name,'======================')
        username = request.POST.get('checkoutusername', '')
        email = request.POST.get('checkoutemail', '')
        address = request.POST.get('address', '') + " " + request.POST.get('address2', '')+ " " + request.POST.get('country', '')+ " " + request.POST.get('city', '')+ " " + request.POST.get('zip', '')
        phone = request.POST.get('phone', '')

        buyer = Buyer(itemsJson=itemsJson, name=name, username=username, email=email, address=address, phone=phone, payment='2', password='2')
        buyer.save()
        thank=True
        id=buyer.buyerID
        return render(request, 'checkout.html', {'thank':thank, 'id':id})
    
    return render (request,'checkout.html',{'product':product})

def orderSuccess(request):
    return render (request,'orderPlaced.html')