from django.shortcuts import render
from django.views.generic.base import View

from .models import Product


class ProductsView(View):
    """Список товаров"""
    def get(self, request):
        product = Product.objects.filter(available=True)
        return render(request, "shop/products.html", {"product_list": product})


class ProductDetailView(View):
    """Полное описание товара"""
    def get(self, request, slug):
        product = Product.objects.get(url=slug)
        return render(request, "shop/product_detail.html", {"product": product})
