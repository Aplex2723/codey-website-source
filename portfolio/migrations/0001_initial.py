# Generated by Django 4.1.2 on 2022-10-16 03:59

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Nombre")),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha de creacion"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Hora de actualizacion"
                    ),
                ),
            ],
            options={
                "verbose_name": "Categoria",
                "verbose_name_plural": "Categorias",
                "ordering": ["created"],
            },
        ),
        migrations.CreateModel(
            name="ProjectModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Titulo")),
                (
                    "client",
                    models.CharField(max_length=255, verbose_name="Cliente/Empresa"),
                ),
                ("project_date", models.DateField(verbose_name="Fecha de elaboracion")),
                (
                    "project_website",
                    models.CharField(
                        default="Sin Enlace",
                        max_length=255,
                        verbose_name="Link del Projecto",
                    ),
                ),
                (
                    "tech_used",
                    ckeditor.fields.RichTextField(verbose_name="Descripccion corta"),
                ),
                (
                    "content",
                    ckeditor.fields.RichTextField(verbose_name="Descripccion larga"),
                ),
                (
                    "images",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="portfolio",
                        verbose_name="Imagenes",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha de creacion"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        default="project-<function uuid4 at 0x000002CF9A5CEB80>",
                        unique=True,
                        verbose_name="URL (sin espacios)",
                    ),
                ),
                (
                    "categories",
                    models.ManyToManyField(
                        default=django.utils.timezone.now,
                        to="portfolio.category",
                        verbose_name="Categoria",
                    ),
                ),
                (
                    "contributors",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Colaboradores",
                    ),
                ),
            ],
            options={
                "verbose_name": "Proyecto",
                "verbose_name_plural": "Proyectos",
                "ordering": ["created"],
            },
        ),
    ]
