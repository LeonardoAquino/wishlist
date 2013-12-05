from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=140)
    url = models.URLField(max_length=250)
    precio = models.IntegerField(default=0)
    es_recomendado = models.BooleanField(default=False)

    def __unicode__(self):
        return self.nombre + " " + self.url


class Proyecto(models.Model):
    titulo = models.CharField(max_length=250, unique=True)
    descripcion = models.TextField()
    creador = models.ForeignKey(User,related_name="creador")
    contribuyentes = models.ManyToManyField(User, related_name="contribuyentes", blank=True, null=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True,auto_now_add=True)
    terminado = models.BooleanField(default = False)
    video_url = models.URLField(max_length=250)
    duracion = models.IntegerField()

    def __unicode__(self):
        return self.titulo + " " + str(self.terminado)

    def get_short_description(self):
        nombre_creador = self.creador.first_name + " " + self.creador.last_name
        return self.titulo + ", por " + nombre_creador


class Categoria(models.Model):
    nombre = models.CharField(max_length=140)

    def __unicode__(self):
        return self.nombre


class Region(models.Model):
    nombre = models.CharField(max_length=140)

    def __unicode__(self):
        return self.nombre


class Comuna(models.Model):
    nombre = models.CharField(max_length=140)
    codigo = models.IntegerField()
    region = models.ForeignKey(Region)

    def __unicode__(self):
        return self.nombre + ", " + self.region.nombre


class TipoCuenta(models.Model):
    nombre = models.CharField(max_length=140)

    def __unicode__(self):
        return self.nombre


class CuentaCorriente(models.Model):
    numero_cuenta = models.IntegerField()
    tipo_cuenta = models.ForeignKey(TipoCuenta)

    def __unicode__(self):
        return self.numero_cuenta + " " + self.tipo_cuenta.nombre


class DetalleUsuario(models.Model):
    usuario = models.ForeignKey(User)
    rut = models.CharField(max_length=40,unique=True)
    comuna = models.ForeignKey(Comuna)
    cuenta_corriente = models.ForeignKey(CuentaCorriente)

    def __unicode__(self):
        nombre_usuario = self.usuario.first_name + " " + self.usuario.last_name
        return nombre_usuario + ", " + self.rut
