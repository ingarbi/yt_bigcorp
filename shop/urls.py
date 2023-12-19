from django.urls import path

from .views import (ProductListView, category_list, products_detail_view,
                    search_products)

app_name = 'shop'

urlpatterns = [
    # path('', products_view, name='products'),
    path('', ProductListView.as_view(), name='products'),
    path("search_products/", search_products, name="search-products"),
    path('search/<slug:slug>/', category_list, name='category-list'),
    path('<slug:slug>/', products_detail_view, name='product-detail'),
]