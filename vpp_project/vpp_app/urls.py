from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('gioi-thieu/', views.about, name='about'),
    path('san-pham/', views.product_list, name='product_list'), 
    path('tin-tuc/', views.news, name='news'),
    path('lien-he/', views.contact, name='contact'), 
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
