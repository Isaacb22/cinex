from django.db import models
from ckeditor.fields import RichTextField

class Notice(models.Model):
    title = models.CharField(verbose_name="Título", max_length=10)
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", upload_to="services")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "noticia"
        verbose_name_plural = "noticias"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title