from django.urls import path

from .views import ItemListView, OrderItemView, ItemDetailView

app_name = 'core'

urlpatterns = [
    path('', ItemListView.as_view(), name='item_list' ),
    path('checkout/', OrderItemView.as_view(), name='checkout-item' ),
    path('product/<slug>/', ItemDetailView.as_view(), name='product' ),   
]