# Generated by Django 2.2.6 on 2019-10-19 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_remove_shippingaddress_save_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='current_address',
            field=models.BooleanField(default=False),
        ),
    ]
