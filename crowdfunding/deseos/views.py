from django.contrib.auth.models import User
from django.views.generic import ListView, TemplateView
from django.shortcuts import render_to_response
from django.template import RequestContext
<<<<<<< HEAD
=======
from django.contrib.auth.models import User

>>>>>>> a03def4f1a018c757ac66ed489cb96a062044413
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


<<<<<<< HEAD
class MisProyectos(ListView):
	model = Lista
	template_name = ""

	def get_comtext_data(self, **kwargs):
		context = super(MisProyectos, self).get_comtext_data(**kwargs)
		tmp = self.model.objects.filter()

index = ProyectosList.as_view()
dashboard = DashboardView.as_view()
misproyectos = MisProyectos.as_view()
=======
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
>>>>>>> a03def4f1a018c757ac66ed489cb96a062044413
