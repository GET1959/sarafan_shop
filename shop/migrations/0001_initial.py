# Generated by Django 5.1.1 on 2024-09-08 12:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=100, verbose_name="Наименование категории")),
                ("slug", models.SlugField(max_length=100, verbose_name="slug")),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="shop/category/images", verbose_name="Изображение"
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200, verbose_name="Наименование продукта")),
                ("slug", models.SlugField(max_length=100, verbose_name="slug")),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="shop/product/images", verbose_name="Изображение"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_cat",
                        to="shop.category",
                        verbose_name="Категория",
                    ),
                ),
                (
                    "subcategory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_sub",
                        to="shop.category",
                        verbose_name="Подкатегория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.CreateModel(
            name="Subcategory",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=100, verbose_name="Наименование подкатегории")),
                ("slug", models.SlugField(max_length=100, verbose_name="slug")),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="shop/subcategory/images", verbose_name="Изображение"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subcategory",
                        to="shop.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Подкатегория",
                "verbose_name_plural": "Подкатегории",
            },
        ),
    ]
