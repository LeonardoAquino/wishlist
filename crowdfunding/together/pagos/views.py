# -*- coding: utf8 -*-
import os, json

from django.contrib.auth.models import User
from django.db import transaction, IntegrityError
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View, TemplateView



class PagoView(TemplateView):
    def get(self, req):
        return HttpResponse("Jelou parkimeter, jelouuuuu")
    def post(self, req):
    	pass

pagos = PagoView.as_view()
