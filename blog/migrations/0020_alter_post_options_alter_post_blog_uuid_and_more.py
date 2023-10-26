# Generated by Django 4.1.2 on 2022-10-17 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0019_alter_post_blog_uuid_alter_post_slug"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={
                "ordering": ["-created"],
                "verbose_name": "Entrada",
                "verbose_name_plural": "Entradas",
            },
        ),
        migrations.AlterField(
            model_name="post",
            name="blog_uuid",
            field=models.UUIDField(
                default="ad83921d-2ad4-42ce-9c94-f1fc23608346", unique=True
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(
                default="blog-ad83921d-2ad4-42ce-9c94-f1fc23608346",
                unique=True,
                verbose_name="URL (sin espacios)",
            ),
        ),
    ]
