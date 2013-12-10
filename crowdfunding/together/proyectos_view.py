from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.views.generic import TemplateView,ListView,View
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User

from .models import Proyecto, TipoProyecto
from .common import is_valid_text, Http500

class MisProyectosView(ListView):
    model = Proyecto
    template_name = "dashboard/mis_proyectos.html"

    def get_context_data(self,**kwargs):
        context = super(MisProyectosView, self).get_context_data(**kwargs)
        mi_usuario = self.request.user
        context["mis_proyectos"] = self.model.objects.filter(creador_id = mi_usuario.id)
        return context


class NuevoProyecto1View(TemplateView):
    def get(self, req, tipo_proyecto):
        req.session["tipo_proyecto_id"] = tipo_proyecto
        return render_to_response("nuevo_proyecto/nuevo_proyecto_paso_1.html",context_instance=RequestContext(req))


class GuardarPasoUno(View):

    @transaction.commit_on_success
    def post(self, req):
        titulo = req.POST.get('titulo')
        descripcion = req.POST.get('descripcion')
        video = req.POST.get('video')
        categoria = req.POST.get('categoria')
        duracion = req.POST.get('tiempo')
        otros_productos = req.POST.get('otros_productos')

        valido = True
        valido = valido and is_valid_text(titulo)
        valido = valido and is_valid_text(descripcion, 500)
        valido = valido and is_valid_text(video, 250)
        valido = valido and is_valid_text(categoria)

        creador_id = self.request.user.id

        if not valido:
            raise Http500()

        self.__guardar_proyecto(titulo, descripcion, creador_id, video, categoria, duracion)
        return redirect("nuevo_proyecto_paso2")

    def __guardar_proyecto(self, titulo, descripcion, creador_id, video, categoria, duracion):
        tipo_proyecto_id = self.request.session.get("tipo_proyecto_id")
        creador = User.objects.get(pk = creador_id)
        tipo_proyecto = TipoProyecto.objects.get(pk = tipo_proyecto_id)

        proyecto = Proyecto()
        proyecto.titulo = titulo
        proyecto.descripcion = descripcion
        proyecto.creador = creador
        proyecto.video_url = video
        proyecto.duracion = duracion
        proyecto.tipo_proyecto = tipo_proyecto
        proyecto.save()


class NuevoProyecto2View(TemplateView):
    template_name = "nuevo_proyecto/nuevo_proyecto_paso_2.html"


mis_proyectos = login_required(MisProyectosView.as_view())
nuevo_proyecto_paso1 = login_required(NuevoProyecto1View.as_view())
guardar_paso1 = login_required(GuardarPasoUno.as_view())
nuevo_proyecto_paso2 = login_required(NuevoProyecto2View.as_view())
terminos_condiciones = login_required(TemplateView.as_view(template_name="dashboard/terminos_y_condiciones.html"))
tipo_proyecto = login_required(TemplateView.as_view(template_name="dashboard/tipo_de_proyecto.html"))
