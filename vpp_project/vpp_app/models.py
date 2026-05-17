from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200) # Trường tên sản phẩm
    sku = models.CharField(max_length=50) # Mã sản phẩm
    description = models.TextField() # Trường mô tả chi tiết

    def __str__(self):
        return self.name # Hiển thị tên sản phẩm khi truy vấn trong trang Admin

class ContactLead(models.Model):
    fullname = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    request_type = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.fullname