# Generated by Django 4.2.3 on 2023-08-07 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_cart_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='grand_total',
            field=models.IntegerField(default=0),
        ),
    ]
