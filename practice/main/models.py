from pyexpat import model
from tabnanny import verbose
from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'uploads',verbose_name='Картинка')

    def __str__(self):
        return self.image.url
