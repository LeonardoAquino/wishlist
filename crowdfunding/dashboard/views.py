from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,ListView
from deseos.models import Lista

class DashboardView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self,**kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        return context


class MisProyectosView(ListView):
    model = Lista
    template_name = "mis_proyectos.html"

    def get_context_data(self,**kwargs):
        context = super(MisProyectosView, self).get_context_data(**kwargs)
        mi_usuario = self.request.user
        print mi_usuario
        context["mis_proyectos"] = self.model.objects.filter(creador_id = mi_usuario.id)
        return context

class MiPerfilView(TemplateView):
    template_name = "mi_perfil.html"


dashboard = login_required(DashboardView.as_view())
mis_proyectos = login_required(MisProyectosView.as_view())
mi_perfil = login_required(MiPerfilView.as_view())
