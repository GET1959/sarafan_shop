from django.contrib import admin

from shop.models import Gallery, Product, Category, Subcategory


@admin.register(Category)
class SectionAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "image"
    )


@admin.register(Subcategory)
class MaterialAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "slug",
        "image"
    )


class GalleryInline(admin.TabularInline):
    fk_name = "product"
    model = Gallery


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline,]
