from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHOICE=[
                ['M','Mobiles'],['L','Laptops'],
                ['BTW','boytopwear'],['BBW','boybottomwear'],
                ['GTW','girltopwear'],['GBW','girlbottomwear'],
                 ]


class Products(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.IntegerField()
    discounted_price=models.IntegerField()
    description=models.TextField(max_length=100)
    brand=models.CharField(max_length=50)
    category=models.CharField(choices=CATEGORY_CHOICE,max_length=200,default='select')
    product_image=models.ImageField(upload_to='product_image')

    def __str__(self):
        return str(self.id)

STATE_CHOICES=(
    ('Andaman & Nicobar Island','Andaman & Nicobar Island'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chandigarh','Chandigarh'),
    ('Kerala','Kerala')
)

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    locality=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=100)

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

class Shopnow(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

STATUS_CHOICE=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
)

class OrderPlace(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    order_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(choices=STATUS_CHOICE,max_length=100)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price






