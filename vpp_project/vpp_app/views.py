from django.shortcuts import render, redirect
from django.utils.timezone import now 
from datetime import timedelta # <-- Nhớ có dòng này để tính mốc 5 phút
from .models import Product, ActiveViewer 
from .forms import ContactForm

# ====================================================================
# HÀM PHỤ TRỢ: Tự động ghi nhận mã máy và thời gian khách đang xem trang
# ====================================================================
def track_active_viewer(request, name):
    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key
    
    viewer, created = ActiveViewer.objects.get_or_create(
        page_name=name, 
        session_key=session_key
    )
    viewer.last_seen = now()
    viewer.save()

# ====================================================================
# CÁC HÀM ĐIỀU HƯỚNG TRANG NGƯỜI DÙNG
# ====================================================================
def home(request):
    track_active_viewer(request, 'Trang Chủ')
    return render(request, 'products/trang_chu.html')

def about(request):
    track_active_viewer(request, 'Trang Giới Thiệu')
    return render(request, "vpp_app/about.html")

def product_list(request):
    track_active_viewer(request, 'Trang Sản Phẩm')
    products = Product.objects.all()
    return render(request, "vpp_app/product_list.html", {"products": products})

def news(request):
    track_active_viewer(request, 'Trang Tin Tức')
    return render(request, "vpp_app/news.html")

def contact(request):
    track_active_viewer(request, 'Trang Liên Hệ')
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        success = True
        form = ContactForm()
    return render(request, "vpp_app/contact.html", {"form": form, "success": success})

# ====================================================================
# HÀM XỬ LÝ TRANG DASHBOARD ADMIN (CÁI BẠN VỪA HỎI NÈ ĐÃ THÊM VÀO ĐÂY)
# ====================================================================
def admin_dashboard(request):
    # Mốc thời gian: Lấy thời điểm hiện tại trừ đi 5 phút
    time_threshold = now() - timedelta(minutes=5)
    
    # Danh sách các trang bạn muốn thống kê
    danh_sach_trang = ['Trang Chủ', 'Trang Giới Thiệu', 'Trang Sản Phẩm', 'Trang Tin Tức', 'Trang Liên Hệ']
    
    active_counts = []
    for name in danh_sach_trang:
        # Lọc ra những người có last_seen lớn hơn hoặc bằng time_threshold
        so_nguoi_dang_xem = ActiveViewer.objects.filter(page_name=name, last_seen__gte=time_threshold).count()
        
        # Đưa vào danh sách hiển thị
        active_counts.append({
            'page_name': name, 
            'count': so_nguoi_dang_xem
        })
    
    context = {
        'active_counts': active_counts,
    }
    # Nhớ sửa lại đúng đường dẫn thư mục templates của bạn (vpp_app/dashboard.html)
    return render(request, 'vpp_app/dashboard.html', context)
