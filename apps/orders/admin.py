from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'payment_method', 'is_paid', 'created_at')
    list_filter = ('payment_method', 'is_paid')
    search_fields = ('user__email', 'id')
    inlines = [OrderItemInline]

    fieldsets = (
        (None, {'fields': ('user', 'total_price', 'payment_method', 'is_paid')}),
        ('Дата', {'fields': ('created_at',)}),
    )
    readonly_fields = ('created_at',)