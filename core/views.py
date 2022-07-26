from django.shortcuts import render
from django.views import View
from .models import Item
from django.views.generic import ListView, DetailView

class ItemListView(ListView):
    model = Item
    template_name = 'home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Item.objects.all()
        return context


class OrderItemView(ListView):
    template_name = 'checkout-page.html'
    model = Item


class OrderItemView(ListView):
    template_name = 'product-page.html'
    model = Item