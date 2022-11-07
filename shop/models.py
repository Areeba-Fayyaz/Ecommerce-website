from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Item (models.Model):
    itemID= models.AutoField
    productName =models.CharField(max_length=300, default='')
    productType= models.CharField(max_length=300, default='')
    description =models.CharField(max_length=300, default='')
    price =models.IntegerField( default='1')
    productImage = models.ImageField(upload_to= 'myShop/Images', default='')

class Seller (models.Model):
    sellerID= models.AutoField
    name =models.CharField(max_length=300, default='')
    email= models.CharField(max_length=300, default='')
    username=models.CharField(max_length=300, default='')
    password=models.CharField(max_length=300, default='')

class Buyer (models.Model):
    buyerID= models.AutoField
    name =models.CharField(max_length=300, default='')
    email= models.CharField(max_length=300, default='')
    username=models.CharField(max_length=300, default='')
    password=models.CharField(max_length=300, default='')
    payment=models.FloatField(default='1')

class Delivery(models.Model):
    deliveryID= models.AutoField
    buyerID=models.IntegerField( default='1')
    name =models.CharField(max_length=300, default='')
    date= models.DateField(default='')
    address=models.CharField(max_length=300, default='')

class Payment(models.Model):
    paymentID= models.AutoField
    deliveryID=models.IntegerField( default='1')
    cardNumber=models.CharField(max_length=300, default='')
    amount=models.FloatField(default='1')
