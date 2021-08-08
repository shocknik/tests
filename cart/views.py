from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from tests_app.models import Test
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, test_id):
    cart = Cart(request)
    test = get_object_or_404(Test, id=test_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(test=test,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
        return redirect('cart:cart_detail')


def cart_remove(request, test_id):
    cart = Cart(request)
    test = get_object_or_404(Test, id=test_id)
    cart.remove(test)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
