# Generated by Django 4.0 on 2022-01-11 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prod_movement', '0003_alter_prod_move_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prod_move',
            options={'ordering': ['-mid']},
        ),
    ]
