from django.shortcuts import render, get_object_or_404
from django.forms import ModelForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from cart.forms import CartAddProductForm
from django.forms import Form

from .models import Category, Product, User
from .form import AddForm


# def index(request):
#     cat = Category.objects.all()[:2]
#     category = Category.objects.all()
#     product = Product.objects.all()[:8]
#     prod = Product.objects.filter(new_models=True)[:4]
#     prod_lt = Product.objects.filter(price__lt=5000)[:4]
#     image = Product.objects.filter(price__lt=5000)
#     paginator = Paginator(image, 1)
#     if 'page' in request.GET:
#         page_num = request.GET['page']
#     else:
#         page_num = 1
#     page = paginator.get_page(page_num)
#     context = {'category': category, 'product': product, 'cat': cat, 'prod': prod, 'prod_lt': prod_lt, 'page': page, 'image': page.object_list}
#     return render(request, 'index.html', context)


class LoopIndex(SuccessMessageMixin, CreateView, ListView):
    model = Product
    context_object_name = 'image'
    template_name = 'index.html'
    paginate_by = 1
    form_class = AddForm
    success_url = reverse_lazy('index')
    success_message  = 'Вы подписались на рассылку!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat'] = Category.objects.all()[:2]
        context['category'] = Category.objects.all()
        context['product'] = Product.objects.all()[:8]
        context['prod'] = Product.objects.filter(new_models=True)[:4]
        context['prod_lt'] = Product.objects.filter(price__lt=5000)[:4]
        context['image'] = Product.objects.filter(price__lt=5000)
        return context

    def get_queryset(self):
        return Product.objects.filter(price__lt=5000)


class UserEmailAdd(CreateView):
    template_name = 'index.html'
    form_class = AddForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


# def by_category(request, category_id):
#     categoryes = Category.objects.all()
#     current_category = Category.objects.get(pk=category_id)
#     product = Product.objects.filter(category=category_id)
#     context = {'categoryes': categoryes, 'product': product, 'current_category': current_category}
#     return render(request, 'by_category.html', context)


class LoopCategory(TemplateView):
    template_name = 'by_category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['product'] = Product.objects.filter(category=context['category_id'])
        context['current_category'] = Category.objects.get(pk=context['category_id'])
        return context


def delivery(request):
    category = Category.objects.all()
    return render(request, 'delivery.html', {'category': category})

class CategoryNew(TemplateView):
    template_name = 'category_all.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['prod_new'] = Product.objects.filter(new_models=True)
        return context


class CategoryPrice(TemplateView):
    template_name = 'price_lt.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['prod_price'] = Product.objects.filter(price__lt=5000)
        return context


# class ProductDetail(Form, DetailView):
#     model = Product
#     template_name = 'detail.html'
#     form_class = CartAddProductForm()
#     success_url = reverse_lazy('cart')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['category'] = Category.objects.all()
#         return context

def detail(request, id):
    product = get_object_or_404(Product, id=id)
    cart_product_form = CartAddProductForm()
    category = Category.objects.all()
    context = {'product': product, 'cart_product_form': cart_product_form, 'category': category}
    return render(request, 'detail.html', context)
