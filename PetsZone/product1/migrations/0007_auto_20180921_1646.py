# Generated by Django 2.1 on 2018-09-21 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product1', '0006_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
