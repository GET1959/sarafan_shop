from rest_framework import serializers
from rest_framework.fields import SerializerMethodField, CharField, FloatField, IntegerField
from rest_framework.serializers import ModelSerializer

from shop.models import Category, Product, Gallery, BasketItem, Basket


class CategorySerializer(ModelSerializer):
    subcategory_list = SerializerMethodField(read_only=True)

    def get_subcategory_list(self, obj):
        if obj.subcategories:
            return [subcat.title for subcat in Category.objects.filter(parent_category=obj)]

    class Meta:
        model = Category
        fields = ("id", "title", "slug", "image", "subcategory_list")


class GallerySerializer(ModelSerializer):
    class Meta:
        model = Gallery
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    gallery = SerializerMethodField(read_only=True)

    def get_gallery(self, obj):
        return [f"image_id-{img.id}" for img in Gallery.objects.filter(product=obj)]

    class Meta:
        model = Product
        fields = ("id", "title", "category", "slug", "price", "gallery")


class CurrentUserDefault:
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context['request'].user


class BasketItemSerializer(ModelSerializer):
    total_price = SerializerMethodField()

    class Meta:
        model = BasketItem
        fields = '__all__'

    def get_total_price(self, instance):
        return instance.sum


class BasketSerializer(ModelSerializer):
    user = serializers.HiddenField(default=CurrentUserDefault())
    product_item = SerializerMethodField()
    basket_total_price = SerializerMethodField

    class Meta:
        model = Basket
        fields = '__all__'

    def get_product_item(self, instance):
        return [
            (item.product.title, item.product.price, item.quantity) for item in BasketItem.objects.filter(basket=instance)
        ]

    def get_basket_total_price(self, instance):
        return instance.sum
