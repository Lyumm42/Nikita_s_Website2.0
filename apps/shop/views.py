import messages
from django.shortcuts import render, get_object_or_404, redirect
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
        'shop/shop.html',
        {'products': products, 'categories': categories}
    )



def product_detail(request, pk=None):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'shop/product_detail.html', context)


def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        quantity = int(request.POST.get('quantity', 1))

        quantity = max(1, min(quantity, 10))

        cart = request.session.get('cart', {})
        product_key = str(product.id)

        if product_key in cart:
            cart[product_key] += quantity
        else:
            cart[product_key] = quantity

        request.session['cart'] = cart
        messages.success(request, f'{product.name} добавлен в корзину!')

        return redirect('product_detail', pk=product_id)

    return redirect('product_detail', pk=product_id)