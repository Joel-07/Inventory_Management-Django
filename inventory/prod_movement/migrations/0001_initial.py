# Generated by Django 4.0 on 2021-12-31 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_remove_products_id_products_pid'),
    ]

    operations = [
        migrations.CreateModel(
            name='prod_move',
            fields=[
                ('mid', models.IntegerField(primary_key=True, serialize=False)),
                ('timestamp', models.CharField(max_length=100)),
                ('f_location', models.CharField(max_length=50)),
                ('t_location', models.CharField(max_length=50)),
                ('qty', models.IntegerField(max_length=50)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.products')),
            ],
        ),
    ]