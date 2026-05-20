from django.db import models
from django.utils.timezone import now

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

class ActiveViewer(models.Model):
    page_name = models.CharField(max_length=100)       # Tên trang web đang xem
    session_key = models.CharField(max_length=255)     # Mã định danh thiết bị của khách
    last_seen = models.DateTimeField(default=now)      # Thời gian nhìn thấy khách lần cuối

    def __str__(self):
        return f"{self.page_name} - Khách: {self.session_key}"
