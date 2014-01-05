from django.db import models
from django.contrib.auth.models import User

class TipoProyecto(models.Model):
    nombre = models.CharField(max_length=140)
    impuesto = models.IntegerField(null=True)

    def __unicode__(self):
        return self.nombre


class Proyecto(models.Model):
    titulo = models.CharField(max_length=250, unique=True)
    descripcion = models.TextField()
    creador = models.ForeignKey(User, related_name="creador")
    contribuyentes = models.ManyToManyField(User, related_name="contribuyentes", blank=True, null=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True, auto_now_add=True)
    terminado = models.BooleanField(default=False)
    video_url = models.URLField(max_length=500)
    duracion = models.IntegerField()
    tipo_proyecto = models.ForeignKey(TipoProyecto)

    def __unicode__(self):
        return self.titulo + " " + str(self.terminado)

    def get_short_description(self):
        nombre_creador = self.creador.first_name + " " + self.creador.last_name
        return self.titulo + ", por " + nombre_creador

    def get_proyecto(self):
        nombre_creador = self.creador.username

        obj = {
            'id': self.id,
            'titulo': self.titulo,
            'creador': nombre_creador,
            'fecha_creacion': self.fecha_creacion,
            'duracion': self.duracion
        }

        return obj


class ImagenProyecto(models.Model):
    imagen = models.FileField(upload_to="proyectos/thumbnails")
    proyecto = models.ForeignKey(Proyecto,null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        if self.proyecto is None:
            return " Sin proyecto " + self.fecha_creacion

        return self.proyecto.titulo + " " + self.fecha_creacion


class Moneda(models.Model):
    nombre = models.CharField(max_length=140)

    def __unicode__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=140)
    url = models.URLField(max_length=500)
    precio = models.IntegerField(default=0)
    moneda = models.ForeignKey(Moneda)
    es_recomendado = models.BooleanField(default=False)
    descripcion = models.TextField()
    proyecto = models.ForeignKey(Proyecto)

    def __unicode__(self):
        return self.nombre + " " + self.url

    def get_producto(self):
        obj = {
            'id': self.id,
            'nombre': self.nombre,
            'url': self.url,
            'precio': self.precio,
            'es_recomendado': self.es_recomendado
        }

        return obj


class ImagenProducto(models.Model):
    imagen = models.FileField(upload_to="productos/thumbnails")
    producto = models.ForeignKey(Producto,null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.producto.nombre + " " + self.fecha_creacion


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


class Banco(models.Model):
    nombre = models.CharField(max_length=140)

    def __unicode__(self):
        return self.nombre


class CuentaBancaria(models.Model):
    numero_cuenta = models.IntegerField()
    tipo_cuenta = models.ForeignKey(TipoCuenta)
    banco = models.ForeignKey(Banco)

    def __unicode__(self):
        return self.numero_cuenta + " " + self.tipo_cuenta.nombre


class DetalleUsuario(models.Model):
    usuario = models.ForeignKey(User)
    rut = models.CharField(max_length=40, unique=True, null=True, blank=True)
    comuna = models.ForeignKey(Comuna, null=True, blank=True)
    sexo = models.BooleanField(default=True)
    cuenta_bancaria = models.ForeignKey(CuentaBancaria, null=True, blank=True)
    fecha_nacimiento = models.DateField()

    def __unicode__(self):
        return self.usuario.username
