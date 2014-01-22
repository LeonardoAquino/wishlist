# -*- coding: utf8 -*-
import os, json

from django.contrib.auth.models import User
from django.db import transaction, IntegrityError
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View, TemplateView

from ..models import ComprobantePago, Mensaje, Proyecto
from ..common import is_text_valid, is_email_valid, is_number_valid


class PagoView(TemplateView):
    def get(self, req):
        return HttpResponse("Jelou parkimeter, jelouuuuu")
    def post(self, req):
    	nombre = req.Post.get("nombre")
    	mensaje = req.Post.get("mensaje")
    	email = req.Post.get("email")
    	monto = req.Post.get("monto")
    	forma_pago = req.Post.get("forma_pago")
    	id_proyecto = req.Post.get("id_proyecto")

    	valido = True
    	valido = valido and is_text_valid(nombre, 140)
    	valido = valido and is_email_valid(email)
    	valido = valido and is_text_valid(mensaje, 500)
    	valido = valido and is_number_valid(monto)

    	if not valido:
    		raise Http500()

    	proyecto = Proyecto.objects.get(pk = id_proyecto)

    	cp = ComprobantePago()
    	cp.nombre = nombre
    	cp.mail = email
    	cp.monto = monto
    	cp.opcion_pago = forma_pago
    	cp.proyecto = proyecto
    	cp.save()

    	m = Mensaje()
    	m.pago = cp
    	m.mensaje = mensaje


    	

pagos = PagoView.as_view()
