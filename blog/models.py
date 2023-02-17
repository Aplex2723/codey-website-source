from django.db import models
import uuid
from django.utils.timezone import now
from django.contrib.auth.models import User
from registration.models import Profile
from ckeditor.fields import RichTextField

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

class Post(models.Model):
    uniqueId = str(uuid.uuid4())
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = RichTextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicacion", default=now)
    image = models.ImageField(verbose_name="Imagen de portada", upload_to="blog", default="placeholder.png")
    
    author = models.ForeignKey(Profile, verbose_name="Autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Hora de actualizacion")

    slug = models.SlugField(unique=True, verbose_name="URL (sin espacios)", default=f"blog-{uniqueId}")
    blog_uuid = models.UUIDField(default=uniqueId, unique=True)

    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ['-created']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.content
    