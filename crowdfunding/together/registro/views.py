#-*- coding: utf-8 -*-
import json
import calendar
from datetime import datetime, date

from django.contrib.auth.models import User
from django.db import transaction, IntegrityError
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View, TemplateView

from ..models import Region, Comuna, DetalleUsuario
from ..common import is_text_valid, is_email_valid

class RegistroView(TemplateView):
    template_name = "registro/registro.html"

    def get_context_data(self, **kw):
        data = super(RegistroView, self).get_context_data(**kw)
        regiones = Region.objects.all()

        data = {
            "regiones" : regiones,
            "comunas" : [],
            "dias" : [i + 1 for i in range(31)],
            "meses" : [],
            "anios" : [i for i in range(1975, datetime.now().year - 15)]
        }

        for monthnumber in range(1,13):
            data["meses"].append({
                "valor" : monthnumber,
                "nombre" : calendar.month_name[monthnumber]
            })

        return data


def obtener_comunas(req):
    region_id = req.GET.get("region")
    comunas = Comuna.objects.filter(region_id=region_id)
    data = []

    for comuna in comunas:
        data.append({
            "id" : comuna.id,
            "nombre" : comuna.nombre
        })

    return HttpResponse(json.dumps(data))


def verificar_usuario(req):
    email = req.GET.get("email")
    username = req.GET.get("username")
    mensaje = None;
    try:
        username_exist = User.objects.get(username = username)
    except User.DoesNotExist as e:
        username_exist = None
        mensaje = "El nombre de usuario ya existe"

    try:
        email_exist = User.objects.get(email = email.lower())
        if mensaje is None:
            mensaje = "El Correo ya existe"
        else:
            mensaje = "Nombre de usuario y correo ya existen"

    except User.MultipleObjectsReturned as mor:
        if mensaje is None:
            mensaje = "El Correo ya existe"
        else:
            mensaje = "Nombre de usuario y correo ya existen"
    except User.DoesNotExist as dne:
        email_exist = None

    data = { "existe" : username_exist is not None, "mensaje" : mensaje }

    return HttpResponse(json.dumps(data))


class EnvioView(View):
    @transaction.commit_on_success
    def post(self, req):
        self.nombre_usuario = req.POST.get("nombre_usuario")
        self.email = req.POST.get("email")
        self.region = req.POST.get("region")
        self.comuna = req.POST.get("comuna")
        self.clave = req.POST.get("password")
        self.sexo = req.POST.get("sexo")
        self.dia = req.POST.get("dia")
        self.mes = req.POST.get("mes")
        self.anio = req.POST.get("anio")

        valido = True
        valido = valido and is_text_valid(self.nombre_usuario)
        valido = valido and is_email_valid(self.email)
        valido = valido and is_text_valid(self.region)
        valido = valido and is_text_valid(self.comuna)
        valido = valido and is_text_valid(self.clave)
        valido = valido and is_text_valid(self.sexo)
        valido = valido and is_text_valid(self.dia)
        valido = valido and is_text_valid(self.mes)
        valido = valido and is_text_valid(self.anio)

        if valido:
            self.__guardar_usuario()

        return render_to_response("registro/registro_exitoso.html")

    def __guardar_usuario(self):
        user = User()
        user.username = self.nombre_usuario
        user.email = self.email.lower()
        user.is_staff = False
        user.is_active = True
        user.set_password(self.clave)
        user.save()

        print "DIA : " + self.dia
        print "MES : " + self.mes
        print "ANIO : " + self.anio

        fecha_nacimiento = date(int(self.anio), int(self.mes), int(self.dia))
        comuna = Comuna.objects.get(pk = self.comuna)

        detalle = DetalleUsuario()
        detalle.fecha_nacimiento = fecha_nacimiento
        detalle.usuario = user
        detalle.comuna = comuna
        detalle.sexo = self.sexo
        detalle.save()

registro = RegistroView.as_view()
envio = EnvioView.as_view()
