# Generated by Django 4.0 on 2022-01-11 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prod_movement', '0002_alter_prod_move_qty'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prod_move',
            options={'ordering': ['mid']},
        ),
    ]
