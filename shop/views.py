from django.shortcuts import render
from shop.models import Category
# Create your views here.

def index(request):
    return render(request,"shop/index.html")

def register(request):
    return render(request,"shop/register.html")

def collection(request):
    category = Category.objects.all().filter(status = 0)
    return render(request,"shop/collection.html",{'category':category})