from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_order, name='create-order'),
    path('success/', views.order_success, name='order_success'),
]