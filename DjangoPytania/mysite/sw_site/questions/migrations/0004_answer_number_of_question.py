# Generated by Django 4.1.3 on 2023-01-30 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_user_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='number_of_question',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
