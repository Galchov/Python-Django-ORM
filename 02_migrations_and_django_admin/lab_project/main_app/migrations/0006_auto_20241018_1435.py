# Generated by Django 5.0.4 on 2024-10-18 13:35
import random

from django.db import migrations


def generate_barcodes(apps, schema_editor):
    Product = apps.get_model('main_app', 'Product')
    all_products = Product.objects.all()
    all_barcodes = random.sample(
        range(100_000_000, 999_999_999),
        len(all_products)
    )
    for product, barcode in zip(all_products, all_barcodes):
        product.barcode = barcode
        product.save()


def reverse_barcodes(apps, schema_editor):
    Product = apps.get_model('main_app', 'Product')
    all_products = Product.objects.all()
    for product in all_products:
        product.barcode = 0
        product.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_product_barcode'),
    ]

    operations = [
        migrations.RunPython(generate_barcodes, reverse_barcodes)
    ]
