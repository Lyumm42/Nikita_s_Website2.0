from django.db import models
from apps.users.models import User
from apps.shop.models import Product

class Order(models.Model):
    PAYMENT_CHOICES = (
        ('cash', 'при получении'),
        ('card', 'Онлайн-оплата'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(choice=PAYMENT_CHOICES)
    is_paid = models.BooleanField(default=False)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()