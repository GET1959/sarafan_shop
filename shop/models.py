from django.conf import settings
from django.db import models

NULLABLE = {"null": True, "blank": True}


class Category(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Наименование категории"
    )
    slug = models.SlugField(
        max_length=100,
        verbose_name="slug"
    )
    image = models.ImageField(
        upload_to="shop/category/images",
        **NULLABLE,
        verbose_name="Изображение"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Subcategory(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Наименование подкатегории"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="subcategory",
        verbose_name="Категория"
    )
    slug = models.SlugField(
        max_length=100,
        verbose_name="slug"
    )
    image = models.ImageField(
        upload_to="shop/subcategory/images",
        **NULLABLE,
        verbose_name="Изображение"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"


class Product(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Наименование продукта"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="product_cat",
        verbose_name="Категория"
    )
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.CASCADE,
        related_name="product_sub",
        verbose_name="Подкатегория"
    )
    slug = models.SlugField(
        max_length=100,
        verbose_name="slug"
    )
    price = models.DecimalField(
        default=0.00,
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Gallery(models.Model):
    image = models.ImageField(
        upload_to="shop/product/images",
        **NULLABLE,
        verbose_name="Изображение"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Продукт"
    )
