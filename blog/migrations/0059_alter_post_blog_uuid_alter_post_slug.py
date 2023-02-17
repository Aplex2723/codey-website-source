# Generated by Django 4.1.2 on 2022-10-22 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0058_alter_post_blog_uuid_alter_post_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="blog_uuid",
            field=models.UUIDField(
                default="6648c52a-3f18-420a-b310-31acea972f52", unique=True
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(
                default="blog-6648c52a-3f18-420a-b310-31acea972f52",
                unique=True,
                verbose_name="URL (sin espacios)",
            ),
        ),
    ]
