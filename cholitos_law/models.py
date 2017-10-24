import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.forms import ModelForm


class Municipality(models.Model):

    name = models.CharField(max_length=200)
    commune = models.CharField(max_length=100)
    region = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    latitud = models.FloatField()
    longitud = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        permissions = (("is_muni", "Can view Munis"),)


class Ong(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    latitud = models.FloatField()
    longitud = models.FloatField()
    municipality = models.ForeignKey(Municipality,
                                     on_delete=models.SET_DEFAULT,
                                     default=''
                                     )

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    image = models.CharField(max_length=200, default='')
    birth = models.DateTimeField()
    description = models.CharField(max_length=500, default='')
    gender = models.CharField(max_length=10, default='hembra')
    ong = models.ForeignKey(Ong, on_delete=models.SET_DEFAULT, default='')

    PERRO = 'Perro'
    GATO = 'Gato'
    OTRO = 'Otro'
    ANIMALS_OPTIONS = (
        (PERRO,'Perro'),
        (GATO,'Gato'),
        (OTRO,'Otro')
    )

    animal_type = models.CharField(max_length=100,choices=ANIMALS_OPTIONS,default=PERRO)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.name

class Complaint(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    gender = models.CharField(max_length=10)
    hurt = models.BooleanField()
    comment = models.CharField(max_length=500)
    image = models.CharField(max_length=200)
    rescue = models.BooleanField()
    municipality = models.ForeignKey(Municipality, on_delete=models.SET_DEFAULT, default='')

    ABANDONO = 'Abandono de Calle'
    EXPOSICION = 'Exposición a temperaturas extremas'
    FAGUA = 'Falta de Agua'
    FCOMIDA = 'Falta de Comida'
    VIOLENCIA = 'Violencia'
    VENTA = 'Venta ambulante'
    TYPES_OPTIONS = (
        (ABANDONO,'Abandono de Calle'),
        (EXPOSICION,'Exposición a temperaturas extremas'),
        (FAGUA,'Falta de Agua'),
        (FCOMIDA,'Falta de Comida'),
        (VIOLENCIA,'Violencia'),
        (VENTA,'Venta ambulante')
    )

    type_complaint = models.CharField(max_length=30,choices=TYPES_OPTIONS,default=ABANDONO)

    PERRO = 'Perro'
    GATO = 'Gato'
    OTRO = 'Otro'
    ANIMALS_OPTIONS = (
        (PERRO,'Perro'),
        (GATO,'Gato'),
        (OTRO,'Otro')
    )

    animals_options = models.CharField(max_length=100,choices=ANIMALS_OPTIONS,default=PERRO)
