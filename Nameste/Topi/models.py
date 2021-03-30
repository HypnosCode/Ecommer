from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from Nameste.settings import MEDIA_ROOT
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    catgories = (
        ('M', 'Mens'),
        ('W', 'Womens')
    )
    sub_cata = (
        ('J', 'JACKET'),
        ('T', 'TSHRIT'),
        ('S', 'SHRIT')
    )
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateTimeField()
    detail = models.TextField()
    clothes_cato = models.CharField(max_length=2, choices=catgories)
    subcatagories = models.CharField(max_length=2, choices=sub_cata)
    image = models.ImageField(upload_to='product/')

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.image.path)
    #     width, height = img.size
    #     print(height, width)
    #     if height != 200 and width != 200:
    #         output_size = (200, 200)
    #         img.thumbnail(output_size)
    #         img.save(MEDIA_ROOT+'/product/resize/'+self.image.name)

    def __str__(self):
        return str(self.id) + '-----' + self.name

    @property
    def imageUrl(self):
        return self.image.url


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/', null=True, blank=True)

    def __str__(self):
        return self.product.name


class Order(models.Model):
    desision = (
        (True, 'Yes'),
        (False, 'No')
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    complete = models.CharField(
        default='False', choices=desision, max_length=5)
    transaction_id = models.CharField(max_length=200)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.qunatity for item in orderitems])
        return total

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = True
        return shipping


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    qunatity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.qunatity
        return total

    def __str__(self):
        return self.product.name


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
