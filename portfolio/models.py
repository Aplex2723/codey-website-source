from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,  verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Hora de actualizacion")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = [('created'), ]

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titulo")
    client = models.CharField(max_length=255, verbose_name="Cliente/Empresa")
    categories = models.ManyToManyField(Category, verbose_name="Categoria")
    project_date = models.DateTimeField(verbose_name="Fecha de elaboracion", default=now)
    project_website = models.URLField(max_length=255, verbose_name="Link del Projecto", default="Sin Enlace")

    tech_used = RichTextField(verbose_name="Descripccion corta")
    content = RichTextField(verbose_name="Descripccion larga")
    images = models.FileField(verbose_name="Imagenes", upload_to="portfolio", null=True, blank=True)
    contributors = models.ManyToManyField(User, verbose_name="Colaboradores")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    slug = models.SlugField(unique=True, verbose_name="URL (sin espacios)", default=f"project-{str(uuid.uuid4())}")

    class Meta:

        verbose_name = ("Proyecto")
        verbose_name_plural = ("Proyectos")
        ordering = [('created')]


    def __str__(self):
        return self.title
