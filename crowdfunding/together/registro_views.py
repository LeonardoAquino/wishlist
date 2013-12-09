#-*- coding: utf-8 -*-
import re
import json

from django.contrib.auth.models import User
from django.db import transaction, IntegrityError
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View

from .models import Region, Comuna
from .common import is_valid_text

def registro(req):
    regiones = Region.objects.all()

    data = {
        "regiones" : regiones,
        "comunas" : []
    }

    return render_to_response("registro/registro.html", data, context_instance = RequestContext(req))


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
    try:
        usuario = User.objects.get(username = req.GET.get("username"))
    except User.DoesNotExist as e:
        usuario = None

    data = { "existe" : usuario is not None }

    return HttpResponse(json.dumps(data))


class EnvioView(View):
    @transaction.commit_on_success
    def post(self, req):
        nombre = req.POST.get('nombre')
        apellido = req.POST.get('apellido')
        rut = req.POST.get('rut')
        email = req.POST.get('email')
        region = req.POST.get('region')
        comuna = req.POST.get('comuna')
        pword = req.POST.get('password')

        valido = True
        valido = valido and is_valid_text(nombre)
        valido = valido and is_valid_text(apellido)
        valido = valido and is_valid_text(rut)
        valido = valido and is_valid_text(region)
        valido = valido and is_valid_text(comuna)
        valido = valido and is_valid_text(pword)
        valido = valido and self.__is_email_valid(email)
        valido = valido and self.__is_rut_valid(rut)

        if valido:
            self.__save_user(nombre, apellido, rut, email, region, comuna, pword)

        return render_to_response("registro/registro_exitoso.html")

    def __save_user(self, nombre, apellido, rut, email, region, comuna, pword):
        user = User()
        user.first_name = nombre
        user.last_name = apellido
        user.email = email
        user.username = email
        user.is_staff = False
        user.is_active = True
        user.set_password(pword)
        user.save()

    def __is_email_valid(self, email):
        return re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,4}$',email.lower())

    def __is_rut_valid(self, rut):
        rut = rut.split('-')
        rut[1] = str(rut[1]).upper()

        value = 11 - sum([ int(a)*int(b) for a,b in zip(str(rut[0]).zfill(8), '32765432')]) % 11
        dv = { 10 : 'K', 11 : '0'}.get(value, str(value))

        return str(dv) == str(rut[1])


envio = EnvioView.as_view()
