from django.db import models
from apps.users.models import User


class Category(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'



class Product(models.Model):
    objects = models.Manager()
    description = models.TextField()
    name = models.CharField(
        max_length=42,
        verbose_name="Название продукта"
    )
    price = models.FloatField(
        default=0,
        verbose_name="Цена"
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='products/'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name



class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"Корзина пользователя {self.user.username}"

    class Meta:
        ordering = ['user']
        verbose_name = 'Корзина'


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} в корзине {self.cart.user.username}"

    def total_price(self):
        return self.quantity * self.product.price


    class Meta:
        ordering = ['cart']
        verbose_name = 'Товар в корзине'
