# Generated by Django 3.2.3 on 2022-05-04 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
