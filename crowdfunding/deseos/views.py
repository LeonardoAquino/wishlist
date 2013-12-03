# Create your views here.
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.shortcuts import render_to_response
from django.template import RequestContext

import json

from .models import Lista

def login(req):
    username = req.POST.get("username")
    password = req.POST.get("password")

    usuario = User.objects.get(username = username, password = password)

    data = {
        "status" : "ok",
        "message" : "",
        "url" : "sadsa"
    }

    if usuario is None:
        data["status"] = "fail"

    return HttpResponse(json.dumps(data))


class ProyectosList(ListView):
    model = Lista
    template_name = "index.html"

    def get_context_data(self,**kwargs):
        context = super(ProyectosList, self).get_context_data(**kwargs)
        context["listas"] = self.model.objects.all()

        return context

index = ProyectosList.as_view()
