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
    parent_category = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        **NULLABLE,
        related_name='subcategories'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


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


class Basket(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='basket'
    )

    @property
    def sum(self):
        return sum(item.sum for item in self.items.all())

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        ordering = ('id',)


class BasketItem(models.Model):
    basket = models.ForeignKey(
        Basket, on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name=None
    )
    quantity = models.PositiveIntegerField(
        default=1
    )

    @property
    def sum(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f'{self.product.title} - {self.quantity}'

    class Meta:
        verbose_name = 'Элемент корзины'
        verbose_name_plural = 'Элементы корзины'
