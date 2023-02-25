# Generated by Django 4.1.3 on 2023-02-23 21:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('image_upload', '0004_alter_expiringlink_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thumbnail',
            name='thumbnail_size',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.CreateModel(
            name='BinaryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('binary_image', models.BinaryField()),
                ('created', models.DateTimeField(null=True)),
                ('expiration_date', models.DateTimeField(null=True)),
                ('seconds_to_expiration', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(300), django.core.validators.MaxValueValidator(30000)])),
                ('base_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image_upload.image')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='image_upload.profile')),
            ],
        ),
    ]