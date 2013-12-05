from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,ListView
from deseos.models import Proyecto

class DashboardView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self,**kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        return context


class MisProyectosView(ListView):
    model = Proyecto
    template_name = "mis_proyectos.html"

    def get_context_data(self,**kwargs):
        context = super(MisProyectosView, self).get_context_data(**kwargs)
        mi_usuario = self.request.user
        context["mis_proyectos"] = self.model.objects.filter(creador_id = mi_usuario.id)
        return context


class MiPerfilView(TemplateView):
    template_name = "mi_perfil.html"


class NuevoProyectoView(TemplateView):
    template_name = "nuevo_proyecto.html"


class GuardarNuevoProyectoView(TemplateView):
    def post(self, req):
        titulo = req.POST.get('titulo')
        descripcion = req.POST.get('descripcion')
        video = req.POST.get('video')
        categoria = req.POST.get('categoria')
        tiempo = req.POST.get('tiempo')
        otros_productos = req.POST.get('otros_productos')

        valido = True
        valido = valido and self.__is_valid(titulo, 140)
        valido = valido and self.__is_valid(descripcion, 500)
        valido = valido and self.__is_valid(video, 250)
        valido = valido and self.__is_valid(categoria, 140)
        #valido = valido and self.__is_valid(tiempo, 140) Falta determinar cantida max.


    def __is_valid(self, texto, largo):
        if texto is None or texto.strip() == "":
            return False

        if len(texto) > largo:
            return False

        return True

dashboard = login_required(DashboardView.as_view())
mis_proyectos = login_required(MisProyectosView.as_view())
mi_perfil = login_required(MiPerfilView.as_view())
nuevo_proyecto = login_required(NuevoProyectoView.as_view())
guardar_nuevo_proyecto = login_required(GuardarNuevoProyectoView.as_view())
