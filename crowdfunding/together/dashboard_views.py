from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,ListView
from .models import Proyecto
from .common import is_valid_text

class DashboardView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self,**kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        return context


class MiPerfilView(TemplateView):
    template_name = "mi_perfil.html"


dashboard = login_required(DashboardView.as_view())
mi_perfil = login_required(MiPerfilView.as_view())
