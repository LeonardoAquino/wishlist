#-*- coding: utf-8 -*-
import re
import json

from django.contrib.auth.models import User
from django.db import transaction, IntegrityError
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View

from deseos.models import Region, Comuna

def registro(req):
    regiones = Region.objects.all()

    data = {
        "regiones" : regiones,
        "comunas" : []
    }

    return render_to_response("registro.html", data, context_instance = RequestContext(req))

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
        
    data = {
        "existe" : usuario is not None
    }

    return HttpResponse(json.dumps(data))

class EnvioView(View):
    def post(self, req):
        nombre = req.POST.get('nombre')
        apellido = req.POST.get('apellido')
        rut = req.POST.get('rut')
        email = req.POST.get('email')
        region = req.POST.get('region')
        comuna = req.POST.get('comuna')
        pword = req.POST.get('password')

        valido = True
        valido = valido and self.__is_valid(nombre)
        valido = valido and self.__is_valid(apellido)
        valido = valido and self.__is_valid(rut)
        valido = valido and self.__is_rut_valid(rut)
        valido = valido and self.__is_valid(email)
        valido = valido and self.__is_valid(region)
        valido = valido and self.__is_valid(comuna)
        valido = valido and self.__is_valid(pword)

        if valido:
            self.__save_user(nombre, apellido, rut, email, region, comuna, pword)

        return render_to_response("registro_exitoso.html")

    @transaction.commit_on_success
    def __save_user(self, nombre, apellido, rut, email, region, comuna, pword):
        try:
            user = User()
            user.first_name = nombre
            user.last_name = apellido
            user.email = email
            user.username = email
            user.is_staff = False
            user.is_active = True
            user.set_password()
            user.save()
        except IntegrityError:
            pass

    def __is_valid(self, texto):
        if texto is None or texto.strip() == "":
            return False

        if len(texto) > 140:
            return False

        return True

    def __is_email_valid(self, email):
        return re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,4}$',email.lower())

    def __is_rut_valid(self, rut):
        rut = rut.split('-')
        rut[1] = str(rut[1]).upper()

        value = 11 - sum([ int(a)*int(b) for a,b in zip(str(rut[0]).zfill(8), '32765432')]) % 11
        dv = { 10 : 'K', 11 : '0'}.get(value, str(value))

        return str(dv) == str(rut[1])


envio = EnvioView.as_view()
