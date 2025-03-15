from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price")
    list_filter = ("category", "price")
    search_fields = ("name", "category")



class CartItemInline(admin.TabularInline):
    model = CartItem
    id_fields = ("product",)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at", "total_items", "total_price")
    inlines = [CartItemInline]

    def total_items(self, obj):
        return obj.cartitem_set.count()
    total_items.short_description = "Товаров в корзине"

    def total_price(self, obj):
        return sum(item.product.price * item.quantity for item in obj.cartitem_set.all())
    total_price.short_description = "Общая стоимость"



@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("cart", "product", "item_price")
    list_filter = ("product",)
    search_fields = ("product__name", "cart__user__email")

    def item_price(self, obj):
        return obj.product.price * obj.count
    item_price.short_description = "Стоимость"