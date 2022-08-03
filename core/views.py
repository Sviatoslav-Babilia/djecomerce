from .models import Item
from django.shortcuts import reverse
from django.views.generic import ListView, DetailView

class ItemListView(ListView):
    model = Item
    template_name = 'home-page.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'product.html'

    # def get_absolute_url(self):
    #     return reverse("core:product", kwargs={
    #         'slug': self.slug
    #     })




class OrderItemView(ListView):
    template_name = 'checkout-page.html'
    model = Item




