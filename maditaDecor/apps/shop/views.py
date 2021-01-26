from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from .models import Product, ProductSerializer


def index(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': products})


def shopping(request):
    products = Product.objects.all()
    return render(request, 'bucket/bucket.html', {'products': products})


@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    data = ProductSerializer(products, many=True)
    return JsonResponse(data.data, safe=False)
