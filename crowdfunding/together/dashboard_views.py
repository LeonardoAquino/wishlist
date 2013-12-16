from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,ListView
from .models import Proyecto, Producto, Categoria
from .common import is_valid_text

class DashboardView(TemplateView):
    template_name = "dashboard/dashboard.html"

    def get_context_data(self,**kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        return context


class MiPerfilView(TemplateView):
    template_name = "dashboard/mi_perfil.html"



class VerProyectoView(TemplateView):
    proyecto = Proyecto
    productos = Producto
    categoria = Categoria
    template_name = ''

    def get(self, req, id_proyecto):
        context = super(VerProyectoView, self).get_context_data(**kwargs)
        context["proyecto"] = self.proyecto.objects.get(id = id_proyecto)
        context["productos"] = self.productos.objects.filter(proyecto = id_proyecto)
        #context['categoria'] = self.categoria.objects.filter()


dashboard = login_required(DashboardView.as_view())
mi_perfil = login_required(MiPerfilView.as_view())
proyecto_detalle = VerProyectoView.as_view()
	