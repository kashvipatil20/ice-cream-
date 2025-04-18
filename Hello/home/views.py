from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from home.models import Product
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def index(request):
    
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc= request.POST.get('desc')
        contact = Contact(name=name,email=email, phone=phone, desc=desc ,date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent successfully!!!")
    return render(request,"contact.html")

def services2(request):
    return render(request,"services2.html")

def services3(request):
    return render(request, "services3.html")
    
def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched', '')
        products = Product.objects.filter(name__icontains=searched)
        return render(request, "search.html", {
            'searched': searched,
            'products': products
        })
    return render(request, "search.html", {})

