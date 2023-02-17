# Generated by Django 4.1.5 on 2023-01-19 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0062_alter_post_blog_uuid_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='blog_uuid',
            field=models.UUIDField(default='16ee2d24-ba35-4d5c-8a03-3120ed64703e', unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='blog-16ee2d24-ba35-4d5c-8a03-3120ed64703e', unique=True, verbose_name='URL (sin espacios)'),
        ),
    ]
