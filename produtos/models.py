from distutils.command.upload import upload
from turtle import title
from venv import create
from django.db import models
#from stdimage.models import StdImageFields

# Create your models here.

class Produto(models.Model):

    title = models.CharField(max_length=255)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    foto = models.ImageField('Imagem', upload_to='fotos')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
