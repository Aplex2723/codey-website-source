# Generated by Django 4.1.2 on 2022-10-15 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_alter_post_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Categoria", "verbose_name_plural": "Categorias"},
        ),
        migrations.AlterModelOptions(
            name="post",
            options={"verbose_name": "Entrada", "verbose_name_plural": "Entradas"},
        ),
    ]
