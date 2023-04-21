from django.db import models
from django.contrib.auth.models import User

class juegos(models.Model):
    nombre = models.TextField (max_length=30)
    descripcion = models.TextField (max_length=500)
    publisher = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='publisher')
    imagen = models.ImageField(upload_to='juegos', null=True, blank=True )

    def __str__(self):
        return f'{self.id} -- {self.nombre} -- {self.descripcion}'


class Profile(models.Model):
    user = models.OneToOneField(to= User, on_delete=models.CASCADE, related_name='profile')
    imagen = models.ImageField(upload_to='profile', null = True, blank=True)

