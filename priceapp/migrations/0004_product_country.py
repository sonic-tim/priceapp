# Generated by Django 4.2.2 on 2023-06-09 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('priceapp', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='priceapp.country', verbose_name='страна'),
            preserve_default=False,
        ),
    ]
