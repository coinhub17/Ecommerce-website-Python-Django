# Generated by Django 3.0.3 on 2020-03-30 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_product_prodslug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRODDiscountPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Discount Price'),
            preserve_default=False,
        ),
    ]
