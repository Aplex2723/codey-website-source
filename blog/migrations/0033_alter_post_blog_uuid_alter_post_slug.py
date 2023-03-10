# Generated by Django 4.1.2 on 2022-10-18 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0032_alter_post_blog_uuid_alter_post_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="blog_uuid",
            field=models.UUIDField(
                default="720b6e9c-7915-4772-a407-fa51252b7521", unique=True
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(
                default="blog-720b6e9c-7915-4772-a407-fa51252b7521",
                unique=True,
                verbose_name="URL (sin espacios)",
            ),
        ),
    ]
