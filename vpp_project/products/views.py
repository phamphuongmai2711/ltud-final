# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Product

# Danh sách sản phẩm
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {'products': products})

# Chi tiết sản phẩm
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/detail.html', {'product': product})