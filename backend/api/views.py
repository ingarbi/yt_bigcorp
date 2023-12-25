from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from recommend.models import Review
from shop.models import Product

from .pagination import StandardResultsSetPagination
from .permissions import IsAdminOrReadOnly
from .serializers import (ProductDetailSerializer, ProductSerializer,
                          ReviewSerializer)

User = get_user_model()
class ProductListApiView(generics.ListAPIView):
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = StandardResultsSetPagination
    serializer_class = ProductSerializer
    queryset = Product.objects.select_related('category').order_by('id')


class ProductDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = "pk"


class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        product_id = self.request.data.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        existing_review = Review.objects.filter(
            product=product, created_by=self.request.user).exists()
        if existing_review:
            raise ValidationError("You have already reviewed this product.")

        serializer.save(created_by=self.request.user, product=product)
