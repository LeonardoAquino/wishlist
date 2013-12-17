from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,ListView
from ..models import Proyecto, Producto, Categoria
from ..common import is_valid_text

class DashboardView(TemplateView):
    template_name = "dashboard/dashboard.html"

    def get_context_data(self,**kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        return context


class MiPerfilView(TemplateView):
    template_name = "dashboard/mi_perfil.html"


class VerProyectoView(TemplateView):
    template_name = 'dashboard/ver_proyecto.html'

    def get_context_data(self, **kwargs):
        context = super(VerProyectoView, self).get_context_data(**kwargs)
        id_proyecto = kwargs.get('id_proyecto')

        obj_proyecto = Proyecto.objects.get(id = id_proyecto)
        context["proyecto"] = obj_proyecto
        context["productos"] = Producto.objects.filter(proyecto = id_proyecto)
        #context['categoria'] = self.categoria.objects.filter(obj_proyecto.id_categoria)
        return context


dashboard = login_required(DashboardView.as_view())
mi_perfil = login_required(MiPerfilView.as_view())
ver_proyecto = VerProyectoView.as_view()