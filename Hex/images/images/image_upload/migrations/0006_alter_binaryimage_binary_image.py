# Generated by Django 4.1.3 on 2023-02-23 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_upload', '0005_alter_thumbnail_thumbnail_size_binaryimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='binaryimage',
            name='binary_image',
            field=models.BinaryField(editable=True),
        ),
    ]