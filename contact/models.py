from django.db import models

# Create your models here.
class ConctactModel(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nombre")
    email = models.EmailField(verbose_name="Correo")
    subject = models.CharField(max_length=255, verbose_name="Asunto")
    content = models.TextField(verbose_name="Descripccion")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de envio")

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ['created']
    
    def __str__(self):
        return self.name
    