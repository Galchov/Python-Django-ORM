# Generated by Django 5.2 on 2025-04-27 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_product_category_alter_product_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='barcode',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
