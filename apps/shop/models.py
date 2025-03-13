from django.db import models

class Category(models.Model):
    objects = None
    name = models.CharField("Название", max_length=100)
    description = ...

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"



class Product(models.Model):
    objects = None
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    name = models.CharField("Название", max_length=200)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField("Изображение", upload_to="products/")
    count = models.PositiveIntegerField("Количество")

    def __str__(self):
        return self.name