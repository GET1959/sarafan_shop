
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from shop.models import Category, Subcategory, Product, Gallery


class CategorySerializer(ModelSerializer):
    subcategory_list = SerializerMethodField(read_only=True)

    def get_subcategory_list(self, obj):
        return [subcategory.title for subcategory in Subcategory.objects.filter(category=obj)]

    class Meta:
        model = Category
        fields = ("id", "title", "slug", "image", "subcategory_list")


class SubcategorySerializer(ModelSerializer):
    class Meta:
        model = Subcategory
        fields = "__all__"


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
        fields = ("id", "title", "category", "subcategory", "slug", "price", "gallery")
