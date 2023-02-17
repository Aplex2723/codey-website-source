# Generated by Django 4.1.2 on 2022-10-16 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0016_alter_post_blog_uuid_alter_post_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="blog_uuid",
            field=models.UUIDField(
                default="db818f09-d487-44a5-968b-c95f6d688af0", unique=True
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(
                default="blog-db818f09-d487-44a5-968b-c95f6d688af0",
                unique=True,
                verbose_name="URL (sin espacios)",
            ),
        ),
    ]
