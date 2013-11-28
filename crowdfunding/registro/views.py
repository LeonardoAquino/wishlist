# Create your views here.
import re
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from deseos.models import Region, Comuna

import json

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

def envio(req):
    nombre = req.POST.get('nombre')
    apellido = req.POST.get('apellido')
    rut = req.POST.get('rut')
    email = req.POST.get('email')
    region = req.POST.get('region')
    comuna = req.POST.get('comuna')
    print isValidEmail(email)

    return HttpResponse("LISTOU")

def isValid(txt):
    if txt is not None:
        return True
    else:
        return False

def isValidEmail(txt):
    if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,4}$',txt.lower()):
        return True
    else:
        return False
