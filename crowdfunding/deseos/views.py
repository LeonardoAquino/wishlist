from django.contrib.auth.models import User
from django.views.generic import ListView, TemplateView
from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import Proyecto


class ProyectosList(ListView):
    model = Proyecto
    template_name = "index.html"

    def get_context_data(self,**kwargs):
        context = super(ProyectosList, self).get_context_data(**kwargs)
        context["proyectos"] = self.model.objects.all()

        return context


class DashboardView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self,**kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        return context


class MisProyectos(ListView):
	model = Proyecto
	template_name = ""

	def get_comtext_data(self, **kwargs):
		context = super(MisProyectos, self).get_comtext_data(**kwargs)
		tmp = self.model.objects.filter()


index = ProyectosList.as_view()
dashboard = DashboardView.as_view()
misproyectos = MisProyectos.as_view()
