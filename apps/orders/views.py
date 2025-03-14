from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from apps.shop.models import Cart


@login_required
def process_payment(request):
    cart = Cart.objects.all(user=request.user)
    cart.products.clear()
    return redirect('order_success')