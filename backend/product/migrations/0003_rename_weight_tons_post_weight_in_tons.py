# Generated by Django 4.1.7 on 2023-03-27 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_post_weight_tons'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='weight_tons',
            new_name='weight_in_tons',
        ),
    ]
