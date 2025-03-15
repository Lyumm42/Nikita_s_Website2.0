from django.shortcuts import render
from .models import Product, Category
from django.db.models import Q

def product_list(request):
    search_query = request.GET.get('search', '')
    category_id = request.GET.get('category')

    products = Product.objects.all()

    if search_query:
        products = products.filter(
            Q(name__icontains=search_query),
            Q(description__icontains=search_query),
        )

    if category_id:
        products = products.filter(category_id=category_id)

    categories = Category.objects.all()

    return render(
        request,
        'shop/product_list.html',
        {'products': products, 'categories': categories}
    )