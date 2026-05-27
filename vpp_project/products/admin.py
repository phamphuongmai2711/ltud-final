from django.contrib import admin
from .models import Product

# Đăng ký model để hiển thị trên trang admin
admin.site.register(Product)
