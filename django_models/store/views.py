from django.shortcuts import render

# Create your views here.
from store.models import Product


def category_view(request, name):
    products = Product.objects.filter(categories__name=name)
    print('_|_' * 20)
    return render(request, 'store/category.html', {'products': products, 'category_name': name})