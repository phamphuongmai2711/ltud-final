from django.db import models
from django.utils.timezone import now

class Product(models.Model):
    name = models.CharField(max_length=200)  # Trường tên sản phẩm
    sku = models.CharField(max_length=50, blank=True, default='')  # Mã sản phẩm
    price = models.IntegerField(default=0)  # Trường giá sản phẩm
    quantity = models.IntegerField(default=0)  # Trường số lượng sản phẩm
    description = models.TextField()  # Trường mô tả chi tiết
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)  # Trường hình ảnh sản phẩm

    def __str__(self):
        return self.name  # Hiển thị tên sản phẩm khi truy vấn trong trang Admin

class ContactLead(models.Model):
    CUSTOMER_TYPE_CHOICES = [
        ('retail', 'Khách mua lẻ'),
        ('business', 'Mua cho Doanh nghiệp / Trường học'),
        ('agency', 'Đăng ký làm đại lý'),
    ]

    REQUEST_TYPE_CHOICES = [
        ('agency_signup', 'Đăng ký đại lý'),
        ('wholesale_quote', 'Nhận báo giá mua sỉ'),
        ('quality_feedback', 'Góp ý chất lượng'),
    ]

    fullname = models.CharField('Họ và tên', max_length=200)
    organization = models.CharField('Công ty / Trường học', max_length=200, blank=True)
    phone = models.CharField('Số điện thoại', max_length=20)
    email = models.EmailField('Email')
    customer_type = models.CharField('Anh/chị đang là', max_length=50, choices=CUSTOMER_TYPE_CHOICES, default='business')
    request_type = models.CharField('Loại yêu cầu', max_length=50, choices=REQUEST_TYPE_CHOICES)
    message = models.TextField('Nội dung yêu cầu')
    created_at = models.DateTimeField('Ngày gửi', auto_now_add=True)

    class Meta:
        verbose_name = 'Lead liên hệ'
        verbose_name_plural = 'Leads liên hệ'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.fullname} - {self.get_request_type_display()}"

class ActiveViewer(models.Model):
    page_name = models.CharField(max_length=100)       # Tên trang web đang xem
    session_key = models.CharField(max_length=255)     # Mã định danh thiết bị của khách
    last_seen = models.DateTimeField(default=now)      # Thời gian nhìn thấy khách lần cuối

    def __str__(self):
        return f"{self.page_name} - Khách: {self.session_key}"
