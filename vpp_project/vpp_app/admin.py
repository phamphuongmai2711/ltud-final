from django.contrib import admin
from .models import Product, ContactLead
from . import models
# Đăng ký model để hiển thị trên trang admin
admin.site.register(Product)
admin.site.register(ContactLead)
