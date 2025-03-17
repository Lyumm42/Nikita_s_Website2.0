from django.db import models
from apps.users.models import User
from apps.shop.models import Product

class Order(models.Model):
    PAYMENT_CHOICES = (
        ('cash', 'При получении'),
        ('card', 'Онлайн-оплата'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=13, choices=PAYMENT_CHOICES)
    is_paid = models.BooleanField(default=False)
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    phone = models.CharField(max_length=13, verbose_name='Телефон')
    address = models.TextField(verbose_name='Адрес')
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество')