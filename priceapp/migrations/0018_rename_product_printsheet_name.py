# Generated by Django 4.2.2 on 2023-06-19 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('priceapp', '0017_alter_missingproduct_ean_alter_product_ean'),
    ]

    operations = [
        migrations.RenameField(
            model_name='printsheet',
            old_name='product',
            new_name='name',
        ),
    ]