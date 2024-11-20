from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from shop.models import Products, Customer, Cart,Shopnow, OrderPlace
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.

class HomeView(View):
    def get(self,request):
        mobile=Products.objects.filter(category='M')
        laptop=Products.objects.filter(category='L')
        boytopwear=Products.objects.filter(category='BTW')
        boybottomwear=Products.objects.filter(category='BBW')
        girltopwear=Products.objects.filter(category='GTW')
        girlbottomwear=Products.objects.filter(category='GBW')

        return render(request,'app/home.html',{'mobile':mobile,'laptop':laptop,'boytop':boytopwear,
                     'boybottom':boybottomwear,'girltop':girltopwear,'girlbottom':girlbottomwear,
                                            })


class PdetailsView(View):
    def get(self,request,pk):
        product=Products.objects.get(pk=pk)
        item_already_in_cart=False
        if request.user.is_authenticated:
            item_already_in_cart=Cart.objects.filter(Q(product=product.id)&Q(user=request.user)).exists()
        return render(request,'app/productdetail.html',{'sproduct':product,'item_already_in_cart':item_already_in_cart})

def mobile(request,data=None):
    if data == None:
        mobile=Products.objects.filter(category='M')
    elif data=='Samsung' or data=='Apple' or data=='Vivo':
        mobile=Products.objects.filter(category='M').filter(brand=data)
    elif data=='above' :
        mobile=Products.objects.filter(category='M').filter(discounted_price__gt=10000)
    elif data=='below':
        mobile=Products.objects.filter(category='M').filter(discounted_price__lt=10000)

    return render(request,'app/mobile.html',{'mobile':mobile})

def laptops(request,data=None):
    if data == None:
        laptops=Products.objects.filter(category='L')
    elif data == 'Dell' or data == 'Lenovo' or data == 'Apple':
        laptops=Products.objects.filter(category='L').filter(brand=data)
    elif data == 'above':
        laptops=Products.objects.filter(category='L').filter(discounted_price__gt=30000)
    elif data == 'below':
        laptops=Products.objects.filter(category='L').filter(discounted_price__lt=30000)

    return render(request,'app/laptop.html',{'laptops':laptops})

def boyt_wears(request,data=None):
    if data==None:
        boytwears=Products.objects.filter(category='BTW')
    elif data == 'above':
        boytwears=Products.objects.filter(category='BTW').filter(discounted_price__gt=500)
    elif data == 'below':
        boytwears=Products.objects.filter(category='BTW').filter(discounted_price__lt=500)
    return render(request,'app/boytopwear.html',{'boytwears':boytwears})

def boyb_wears(request,data):
    if data=='All':
        boyb_wears=Products.objects.filter(category='BBW')
    elif data=='above':
        boyb_wears=Products.objects.filter(category='BBW').filter(discounted_price__gt=500)
    elif data=='below':
        boyb_wears=Products.objects.filter(category='BBW').filter(discounted_price__lt=500)
    return render(request,'app/boybottomwear.html',{'boybottoms':boyb_wears})

def girlt_wears(request,data):
    if data=='All':
        girlt_wears=Products.objects.filter(category='GTW')
    elif data=='above':
        girlt_wears=Products.objects.filter(category='GTW').filter(discounted_price__gt=500)
    elif data=='below':
        girlt_wears=Products.objects.filter(category='GTW').filter(discounted_price__lt=500)
    return render(request,'app/girltopwear.html',{'girltops':girlt_wears})
def girlb_wears(request,data):
    if data=='All':
        girlb_wears=Products.objects.filter(category='GBW')
    elif data=='above':
        girlb_wears=Products.objects.filter(category='GBW').filter(discounted_price__gt=500)
    elif data=='below':
        girlb_wears=Products.objects.filter(category='GBW').filter(discounted_price__lt=500)

    return render(request,'app/girlbottomwear.html',{'girlbottoms':girlb_wears})

class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',{'form':form})
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations!! Registered Successfully')
            form.save()
        return render(request,'app/customerregistration.html',{'form':form})

@method_decorator(login_required,name="dispatch")
def profile(request):
 return render(request, 'app/profile.html')


class ProfileView(View):
    def get(self,request):
        form=CustomerProfileForm()
        return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})
    def post(self,request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            usr=request.user
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            state=form.cleaned_data['state']
            zipcode=form.cleaned_data['zipcode']
            reg=Customer(user=usr,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,'Congratulation!! Profile Updated Successfully')
        return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})

def address(request):
    add=Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html',{'add':add,'active':'btn-primary'})


def add_to_cart(request):
    user=request.user
    if user.is_authenticated:
        product_id=request.GET.get('prod_id')
        product=Products.objects.get(id=product_id)
        Cart(user=user,product=product).save()
        return redirect('/cart')
    else:
        return redirect('/')

def shop_now(request):
    if request.user.is_authenticated:
        user = request.user
        product_id = request.GET.get('prod_id')
        p = Products.objects.get(id=product_id)
        Shopnow(user=user, product=p).save()

        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        tempamount = (1* p.discounted_price)
        amount += tempamount
        totalamount = amount + shipping_amount
        return render(request,'app/shopnow.html',{'p':p,'totalamount':totalamount,'amount':amount})

@login_required
def show_cart(request):

    if request.user.is_authenticated:
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount=0.0
        shipping_amount=70.0
        total_amount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount=(p.quantity * p.product.discounted_price )
                amount+=tempamount
                totalamount=amount+shipping_amount
            return render(request,'app/addtocart.html',{'carts':cart,'totalamount':totalamount,'amount':amount})
        else:
            return render(request, 'app/emptycart.html')

def plus_cart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        if Cart.objects.filter(product=prod_id):
            c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
            c.quantity+=1
            c.save()
            amount = 0.0
            shipping_amount = 70.0
            total_amount = 0.0
            user = request.user
            cart_product = [p for p in Cart.objects.all() if p.user == user]
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
            data={
                'quantity':p.quantity,
                'amount':amount,
                'totalamount':amount + shipping_amount,
                }
            return JsonResponse(data)
        elif Shopnow.objects.get(product=prod_id):
            c = Shopnow.objects.get(Q(product=prod_id) & Q(user=request.user))
            c.quantity += 1
            c.save()
            amount = 0.0
            shipping_amount = 70.0
            total_amount = 0.0
            user = request.user
            cart_product = [p for p in Shopnow.objects.all() if p.user == user]
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
            data = {
                'quantity': p.quantity,
                'amount': amount,
                'totalamount': amount + shipping_amount,
            }
            return JsonResponse(data)


def minus_cart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        if Cart.objects.filter(product=prod_id):

            c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
            c.quantity-=1
            c.save()
            amount = 0.0
            shipping_amount = 70.0
            total_amount = 0.0
            user = request.user
            cart_product = [p for p in Cart.objects.all() if p.user == user]
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
            data={
                'quantity':c.quantity,
                'amount':amount,
                'totalamount':amount + shipping_amount,
                }
            return JsonResponse(data)
        else:
            c = Shopnow.objects.get(Q(product=prod_id) & Q(user=request.user))
            c.quantity -= 1
            c.save()
            amount = 0.0
            shipping_amount = 70.0
            total_amount = 0.0
            user = request.user
            cart_product = [p for p in Shopnow.objects.all() if p.user == user]
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
            data = {
                'quantity': p.quantity,
                'amount': amount,
                'totalamount': amount + shipping_amount,
            }
            return JsonResponse(data)

def remove_cart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        if Cart.objects.filter(product=prod_id):

            c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
            c.delete()
            amount = 0.0
            shipping_amount = 70.0
            total_amount = 0.0
            user = request.user
            cart_product = [p for p in Cart.objects.all() if p.user == user]
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
            data={
                'amount':amount,
                'totalamount':amount + shipping_amount,
                }
            return JsonResponse(data)
        else:
            c = Shopnow.objects.get(Q(product=prod_id) & Q(user=request.user))
            c.quantity += 1
            c.delete()
            amount = 0.0
            shipping_amount = 70.0
            total_amount = 0.0
            user = request.user
            cart_product = [p for p in Shopnow.objects.all() if p.user == user]
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
            data = {
                'amount': amount,
                'totalamount': amount + shipping_amount,
            }
            return JsonResponse(data)

def checkout(request):
    user = request.user
    add=Customer.objects.filter(user=user)
    if Cart.objects.filter(user=user):
        cart_item=Cart.objects.filter(user=user)
        amount=0.0
        shipping_amount=70.0
        totalamount=0.0

        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
            totalamount=amount+shipping_amount
        return render(request, 'app/checkout.html',{'add':add,'totalamount':totalamount,'cartitem':cart_item})

    else:
        p = Shopnow.objects.get(user=user)
        amount = 0.0
        shipping_amount = 70.0
        totalamount = 0.0
        tempamount = (p.quantity * p.product.discounted_price)
        amount += tempamount
        totalamount = amount + shipping_amount

        return render(request, 'app/checkout.html',{'add':add,'totalamount':totalamount,'p':p})

def payment_done(request):
    user=request.user
    custid = request.GET.get('custid')
    customer=Customer.objects.get(id=custid)
    if Cart.objects.filter(user=user):
        cart=Cart.objects.filter(user=user)
        for c in cart:
            OrderPlace(user=user,customer=customer,product=c.product,quantity=c.quantity).save()
            c.delete()
        return redirect("orders")
    else:
        c = Shopnow.objects.get(user=user)
        OrderPlace(user=user, customer=customer, product=c.product, quantity=c.quantity).save()
        c.delete()
        return redirect("orders")

@login_required
def orders(request):
    op=OrderPlace.objects.filter(user=request.user)
    return render(request, 'app/orders.html',{'order_placed':op})

def cart_number(request):

    if request.user.is_authenticated:
        cart_items_count = Cart.objects.filter(user=request.user).count()
    else:
        cart_items_count = 0
    return {'cart_items_count': cart_items_count}
































