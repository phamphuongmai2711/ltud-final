from django import forms
from .models import ContactLead

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactLead
        fields = ['fullname', 'organization', 'phone', 'email', 'customer_type', 'request_type', 'message']
        labels = {
            'fullname': 'Họ và tên',
            'organization': 'Công ty / Trường học',
            'phone': 'Số điện thoại',
            'email': 'Email',
            'customer_type': 'Anh/chị đang là',
            'request_type': 'Loại yêu cầu',
            'message': 'Nội dung tin nhắn chi tiết',
        }
        widgets = {
            'fullname': forms.TextInput(attrs={'placeholder': 'Nhập họ và tên hoặc tên người liên hệ'}),
            'organization': forms.TextInput(attrs={'placeholder': 'Tên công ty hoặc tên trường học'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Ví dụ: 0909 123 456'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Ví dụ: lienhe@vanphongpham.com'}),
            'customer_type': forms.Select(attrs={'class': 'form-select'}),
            'request_type': forms.Select(attrs={'class': 'form-select'}),
            'message': forms.Textarea(attrs={'placeholder': 'Mô tả chi tiết yêu cầu, ngành hàng, số lượng, thời gian cần báo giá...', 'rows': 6}),
        }




