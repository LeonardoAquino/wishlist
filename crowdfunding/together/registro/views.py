#-*- coding: utf-8 -*-
import json

from django.contrib.auth.models import User
from django.db import transaction, IntegrityError
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View

from ..models import Region, Comuna
from ..common import is_text_valid, is_email_valid

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
        email = req.POST.get('email')
        region = req.POST.get('region')
        comuna = req.POST.get('comuna')
        pword = req.POST.get('password')

        valido = True
        valido = valido and is_text_valid(nombre)
        valido = valido and is_text_valid(apellido)
        valido = valido and is_text_valid(region)
        valido = valido and is_text_valid(comuna)
        valido = valido and is_text_valid(pword)
        valido = valido and is_email_valid(email)

        if valido:
            self.__save_user(nombre, apellido, email, region, comuna, pword)

        return render_to_response("registro/registro_exitoso.html")

    def __save_user(self, nombre, apellido, email, region, comuna, pword):
        user = User()
        user.first_name = nombre
        user.last_name = apellido
        user.email = email
        user.username = email
        user.is_staff = False
        user.is_active = True
        user.set_password(pword)
        user.save()


envio = EnvioView.as_view()
