from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.product_list, name='product_list'),
]