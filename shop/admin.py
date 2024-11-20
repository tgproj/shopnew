from django.contrib import admin
from shop.models import (Products,Customer,Cart,Shopnow,OrderPlace)
# Register your models here.

@admin.register(Products)
class ProductsModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','selling_price','discounted_price','description','brand','category']
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','zipcode','state']
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']
@admin.register(Shopnow)
class ShopnowModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']
@admin.register(OrderPlace)
class OrderPlaceModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','product','quantity','order_date','status']

