# Generated by Django 4.1.2 on 2022-10-18 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0051_alter_post_blog_uuid_alter_post_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="blog_uuid",
            field=models.UUIDField(
                default="8a1ffc64-3348-4047-a302-bdb9a184528e", unique=True
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(
                default="blog-8a1ffc64-3348-4047-a302-bdb9a184528e",
                unique=True,
                verbose_name="URL (sin espacios)",
            ),
        ),
    ]