# Generated by Django 4.0 on 2022-01-11 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_products_id_products_pid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['pid']},
        ),
    ]
