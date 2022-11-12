from django.contrib import admin

# Register your models here.
from .models import Item,Seller,Buyer,Delivery,Payment
# ,Buyer,Seller,Delivery,Payment
admin.site.register(Item)
admin.site.register(Buyer)

admin.site.register(Seller)
admin.site.register(Delivery)
admin.site.register(Payment)