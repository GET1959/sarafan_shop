from django.contrib import admin

from shop.models import Gallery, Product, Category  # , Subcategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "image",
        "parent_category"
    )


class GalleryInline(admin.TabularInline):
    fk_name = "product"
    model = Gallery


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline,]
    list_display = (
        "title",
        "slug",
        "category"
    )
