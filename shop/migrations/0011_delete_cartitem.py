# Generated by Django 5.1.1 on 2024-09-15 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0010_alter_cartitem_product"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CartItem",
        ),
    ]
