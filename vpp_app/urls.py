from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('san-pham/', views.product_list, name='product_list'),
    path('san-pham/<int:pk>/', views.product_detail, name='product_detail'),
    path('about/', views.about, name='about'),
    path('gioi-thieu/', views.about, name='about_vn'),
    path('tin-tuc/', views.news, name='news'),
    path('lien-he/', views.contact, name='contact'), 
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
