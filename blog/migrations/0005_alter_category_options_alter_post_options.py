# Generated by Django 4.1.2 on 2022-10-15 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_alter_post_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ["created"],
                "verbose_name": "Categoria",
                "verbose_name_plural": "Categorias",
            },
        ),
        migrations.AlterModelOptions(
            name="post",
            options={
                "ordering": ["published"],
                "verbose_name": "Entrada",
                "verbose_name_plural": "Entradas",
            },
        ),
    ]
