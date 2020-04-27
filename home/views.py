from django.shortcuts import render,get_object_or_404
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

    context = {
        'posts1': Product.objects.all().filter(prod_category=1),
        'posts2': Product.objects.all().filter(prod_category=2),
        'posts3': Product.objects.all().filter(prod_category=3),
        'posts4': Product.objects.all().filter(prod_category=4),
        'posts5': Product.objects.all().filter(prod_category=5),
        'posts6': Product.objects.all().filter(prod_category=6),
        'posts7': Product.objects.all().filter(prod_category=7),
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


