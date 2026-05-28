from django.contrib import admin  # type: ignore[import]
from .models import Product, ContactLead


@admin.register(ContactLead)
class ContactLeadAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'organization', 'customer_type', 'request_type', 'phone', 'email', 'created_at')
    list_filter = ('customer_type', 'request_type', 'created_at')
    search_fields = ('fullname', 'organization', 'phone', 'email', 'message')
    date_hierarchy = 'created_at'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku')
    search_fields = ('name', 'sku')
#######################

from .models import Product, Category, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date')
    search_fields = ('title',)