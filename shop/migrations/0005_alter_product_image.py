# Generated by Django 4.2.4 on 2023-12-19 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='products/products/default.jpg', upload_to='images/products/%Y/%m/%d', verbose_name='Изображение'),
        ),
    ]