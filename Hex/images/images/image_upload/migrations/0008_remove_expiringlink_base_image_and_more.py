# Generated by Django 4.1.3 on 2023-02-24 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_upload', '0007_alter_binaryimage_binary_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expiringlink',
            name='base_image',
        ),
        migrations.RemoveField(
            model_name='expiringlink',
            name='created_by',
        ),
        migrations.DeleteModel(
            name='BinaryImage',
        ),
        migrations.DeleteModel(
            name='ExpiringLink',
        ),
    ]
