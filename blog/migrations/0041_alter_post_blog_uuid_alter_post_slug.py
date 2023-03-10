# Generated by Django 4.1.2 on 2022-10-18 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0040_alter_post_blog_uuid_alter_post_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="blog_uuid",
            field=models.UUIDField(
                default="3bf7ada2-8158-447c-aafe-0400357c9898", unique=True
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(
                default="blog-3bf7ada2-8158-447c-aafe-0400357c9898",
                unique=True,
                verbose_name="URL (sin espacios)",
            ),
        ),
    ]
