# Generated by Django 5.0.4 on 2024-10-18 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_product_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='count',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default='No Category', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='supplier',
            field=models.CharField(default='No Supplier', max_length=150),
            preserve_default=False,
        ),
    ]
