# Generated by Django 3.2.8 on 2021-10-14 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20211014_1941'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'permissions': [('cancel_order', 'Can cancel order')]},
        ),
    ]
