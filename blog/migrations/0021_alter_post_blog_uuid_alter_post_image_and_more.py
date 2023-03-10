# Generated by Django 4.1.2 on 2022-10-17 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0020_alter_post_options_alter_post_blog_uuid_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="blog_uuid",
            field=models.UUIDField(
                default="61f685e4-08e3-4d35-bdec-a1e605071cc5", unique=True
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(
                default="placeholder.png",
                upload_to="blog",
                verbose_name="Imagen de portada",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(
                default="blog-61f685e4-08e3-4d35-bdec-a1e605071cc5",
                unique=True,
                verbose_name="URL (sin espacios)",
            ),
        ),
    ]
