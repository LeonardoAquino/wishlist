# Create your views here.
from django.views.generic import ListView
from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import Lista

class ProyectosList(ListView):
    model = Lista
    template_name = "index.html"

    def get_context_data(self,**kwargs):
        context = super(ProyectosList, self).get_context_data(**kwargs)
        context["listas"] = self.model.objects.all()

        return context

index = ProyectosList.as_view()
