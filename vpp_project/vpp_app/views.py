from django.shortcuts import render, redirect
from .models import Product
from .forms import ContactForm

def home(request):
    return render(request, "vpp_app/home.html")

def about(request):
    return render(request, "vpp_app/about.html")

def product_list(request):
    products = Product.objects.all()
    return render(request, "vpp_app/product_list.html", {"products": products})

def news(request):
    return render(request, "vpp_app/news.html")

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid(): # Đã nhập dữ liệu để gửi liên hệ
        form.save()
        return redirect("home")
    return render(request, "vpp_app/contact.html", {"form": form})