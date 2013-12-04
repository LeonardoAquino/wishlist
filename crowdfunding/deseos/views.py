from django.views.generic import ListView, TemplateView
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User

from .models import Lista


class ProyectosList(ListView):
    model = Lista
    template_name = "index.html"

    def get_context_data(self,**kwargs):
        context = super(ProyectosList, self).get_context_data(**kwargs)
        context["listas"] = self.model.objects.all()

        return context


class DashboardView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self,**kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        return context


class MisProyectosView(ListView):
    model = Lista
    template_name = "mis_proyectos.html"

    def get_context_data(self, **kwargs):
        context = super(ProyectosList, self).get_context_data(**kwargs)
        #context["mis_proyectos"] = self.model.objects.filter(creador = )
        print self.request

        return context

index = ProyectosList.as_view()
dashboard = DashboardView.as_view()
mis_proyectos = MisProyectosView.as_view()
