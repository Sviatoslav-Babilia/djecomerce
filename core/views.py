from django.shortcuts import render
from .models import Item
from django.views.generic.list import ListView

class ItemListView(ListView):
    model = Item
    template_name = 'item_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Item.objects.all()
        return context

