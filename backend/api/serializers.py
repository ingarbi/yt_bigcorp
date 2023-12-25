from django.contrib.auth import get_user_model
from rest_framework import serializers

from recommend.models import Review
from shop.models import Category, Product

User = get_user_model()


class ProductSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    category = serializers.SlugRelatedField(
        many=False,
        slug_field="name",
        queryset=Category.objects.all(),
    )
    class Meta:
        model = Product
        fields = ["id", "title", "brand", "image", "category", "price", "created_at", "updated_at"]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','rating', 'content', 'created_by', 'created_at','product_id']
        read_only_fields = ['id', 'created_by', 'created_at']

class ProductDetailSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    category = serializers.SlugRelatedField(
        many=False,
        slug_field="name",
        queryset=Category.objects.all()
    )
    discounted_price = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ["id", "title", "slug", "brand", "category", "price",
                  "image", "available", "discount", "created_at", "updated_at", "discounted_price", "reviews"]

    def get_discounted_price(self, obj):
        discounted_price = obj.get_discounted_price()
        return str(discounted_price)
    
class CustomUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        email = validated_data['email']
        username = email.split('@')[0]
        user = User(
            email=email,
            username=username,
        )
        user.set_password(validated_data['password'])
        user.save()
        return user