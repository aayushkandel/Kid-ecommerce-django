from django.shortcuts import render

def home(request):
    return render(request,"pages/home.html")

def about(request):
    return render(request,"pages/about.html")

def shop(request):
    return render(request,"pages/shop.html")

def news(request):
    return render(request,"pages/news.html")

def contact(request):
    return render(request,"pages/contact.html")

def product(request):
    return render(request,"pages/product.html")