# Create your views here.
#from django.core.context_processors import csrf
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

    return HttpResponse("LISTOU")
