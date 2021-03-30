from django.shortcuts import render
from django.views.generic import ListView, View
from .models import *
from django.http import JsonResponse
import json
from Login.models import *
from .utils import *
import datetime
# Create your views here.


# def index(request):
#     return render(request, 'Topi/index.html', {})


class index(View):
    template_name = 'Topi/index.html'

    def get(self, request):
        context = {}
        context['user'] = self.request.user
        context['productobj'] = Product.objects.order_by('-date')
        context['totalproduct'] = len(Product.objects.all())

        data = cartData(request)
        # print(data)

        cartItems = data['cartItems']

        context['cartItems'] = cartItems
        return render(request, self.template_name, context)

    def post(self, request):
        context = {}
        context['user'] = self.request.user
        context['productobj'] = Product.objects.order_by('-date')
        context['totalproduct'] = len(Product.objects.all())
        return render(request, self.template_name, context)


class shop(ListView):
    model = Customer
    template_name = 'Topi/cart.html'
    context_object_name = 'cart'


class cart(View):
    template_name = 'Topi/cart.html'

    def get(self, request):
        data = cartData(request)

        cartItems = data['cartItems']
        order = data['order']
        items = data['items']
        # print(items)

        context = {'items': items, 'order': order, 'cartItems': cartItems}
        return render(request, self.template_name, context)


class checkout(View):
    template_name = 'Topi/checkout.html'

    def get(self, request):
        data = cartData(request)

        cartItems = data['cartItems']
        order = data['order']
        items = data['items']
        user = data['user']
        context = {'items': items, 'order': order,
                   'cartItems': cartItems, 'users': user}
        context['user'] = self.request.user
        return render(request, self.template_name, context)


class updateItem(View):

    def post(self, request):
        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']
        # print("Action :", action)
        # print('ProductId :', productId)

        customer = request.user.customer
        product = Product.objects.get(id=productId)
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)

        orderItem, created = OrderItem.objects.get_or_create(
            order=order, product=product)

        if action == 'add':
            orderItem.qunatity = (orderItem.qunatity + 1)
        elif action == 'remove':
            orderItem.qunatity = (orderItem.qunatity - 1)

        orderItem.save()

        if orderItem.qunatity <= 0:
            orderItem.delete()

        return JsonResponse('Item was Added to cart', safe=False)


class processOrder(View):
    def post(self, request):
        transaction_id = datetime.datetime.now().timestamp()
        data = json.loads(request.body)

        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(
                customer=customer, complete=False)

        else:
            customer, order = guestOrder(request, data)

        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == float(order.get_cart_total):
            order.complete = 'Yes'
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )
        return JsonResponse('Payment submitted', safe=False)
