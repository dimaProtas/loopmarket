from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from loop.models import Product, Category
from .cart import Cart
from .forms import CartAddProductForm
from django.http import HttpResponseRedirect
from django.contrib import messages

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    messages.info(request, 'Товар добавлен в корзину!')
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail') # HttpResponseRedirect(request.META.get('HTTP_REFERER')) редирект на туже страницу


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.info(request, 'Товар удален из корзины!')
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    category = Category.objects.all()
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'cart/detail.html', {'cart': cart, 'category': category})
