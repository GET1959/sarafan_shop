# Generated by Django 5.1.1 on 2024-09-13 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0006_alter_cartitem_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="cartitem",
            name="total_price",
            field=models.IntegerField(blank=True, null=True, verbose_name="Сумма по продукту"),
        ),
    ]
