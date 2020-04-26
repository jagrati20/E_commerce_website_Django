from django.shortcuts import render
from .models import Product

posts=[
    {
        'product_name':'Shoes',
        'summary':'This is a test Product',
        'price':'some dollars'

    },
    {
        'product_name':'Shirt',
        'summary':'This is a test Product',
        'price':'some dollars!!'

    }
]

def homepage(request):
    context = {
        'posts': posts
    }
    return render(request,'home/home.html',context)

def shopping(request):
    print(request)
    context = {

        'posts': Product.objects.all().filter(prod_category=2)
    }
    return render(request,'home/shop.html',context)


def checkout(request):
    context = {
        'posts': posts
    }
    return render(request, 'home/checkout.html', context)

def cart(request):
    context = {
        'posts': posts
    }
    return render(request, 'home/cart.html', context)

def contact(request):
    context = {
        'posts': posts
    }
    return render(request, 'home/contact.html', context)