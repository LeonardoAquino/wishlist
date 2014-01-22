# -*- coding: utf8 -*-
import os, json

from django.contrib.auth.models import User
from django.db import transaction, IntegrityError
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View, TemplateView

from ..models import ComprobantePago, mensaje
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

    	valido = True
    	valido = valido and is_text_valid(nombre, 140)
    	valido = valido and is_email_valid(email)
    	valido = valido and is_text_valid(mensaje, 500)
    	valido = 


    	

pagos = PagoView.as_view()
