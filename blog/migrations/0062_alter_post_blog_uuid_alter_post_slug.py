# Generated by Django 4.1.5 on 2023-01-19 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0061_alter_post_blog_uuid_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='blog_uuid',
            field=models.UUIDField(default='946ab872-54de-454f-84a7-8bac2570e250', unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='blog-946ab872-54de-454f-84a7-8bac2570e250', unique=True, verbose_name='URL (sin espacios)'),
        ),
    ]
