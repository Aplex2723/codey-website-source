# Generated by Django 4.1.2 on 2022-10-15 01:09

from django.db import migrations
import django.db.models.functions.text


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_alter_category_options_alter_post_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": [django.db.models.functions.text.Upper("created")],
                "verbose_name": "Categoria",
                "verbose_name_plural": "Categorias",
            },
        ),
        migrations.AlterModelOptions(
            name="post",
            options={
                "ordering": [django.db.models.functions.text.Upper("created")],
                "verbose_name": "Entrada",
                "verbose_name_plural": "Entradas",
            },
        ),
    ]
