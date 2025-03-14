from django.shortcuts import render
from .models import Product, Category


def product_list(request):
    category_id = request.GET.get('category', None)
    products = Product.objects.all()

    if category_id:
        products = products.filter(category_id=category_id)

    categories = Category.objects.all()
    return render(request, 'shop/shop.html', {'products': products, 'categories': categories})