from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField()

    class Meta:
        verbose_name = "Пользователь"