# Generated by Django 3.0.3 on 2020-05-05 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0003_remove_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
