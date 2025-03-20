from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.shop.models import Cart, CartItem
from .forms import OrderForm
from .models import OrderItem


@login_required
def create_order(request):
    cart = Cart.objects.get(user=request.user)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = cart.total_price()
            order.save()

            for item in cart.products.all():
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity
                )

            cart.products.clear()

            return redirect('order_success')
    else:
        form = OrderForm()

    return render(request, 'orders/orders.html', {
        'form': form,
        'cart': cart
    })


def order_success(request):
    return render(request, 'orders/success.html')