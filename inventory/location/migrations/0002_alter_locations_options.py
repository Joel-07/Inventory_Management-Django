# Generated by Django 4.0 on 2022-01-11 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='locations',
            options={'ordering': ['lid']},
        ),
    ]
