
from django.views.generic import ListView
from django.shortcuts import render
from products.models import Product
from django.http import HttpResponse


class ProductListView(ListView):
    model = Product
