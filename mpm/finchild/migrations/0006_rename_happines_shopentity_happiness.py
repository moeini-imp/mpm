# Generated by Django 5.0 on 2023-12-07 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finchild', '0005_shopentity_happines'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopentity',
            old_name='happines',
            new_name='happiness',
        ),
    ]