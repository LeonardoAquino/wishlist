from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.views.generic import TemplateView,ListView
from django.shortcuts import render_to_response
from django.template import RequestContext

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


class GuardarPasoUno(TemplateView):
    @transaction.commit_on_success
    def post(self, req):
        titulo = req.POST.get('titulo')
        descripcion = req.POST.get('descripcion')
        video = req.POST.get('video')
        categoria = req.POST.get('categoria')
        duracion = req.POST.get('tiempo')
        #otros_productos = req.POST.get('otros_productos')

        #producto_0
        nombre_producto = req.POST.get("nombre_0")
        url_producto = req.POST.get("url_0")
        desc_producto = req.POST.get("descripcion_0")
        tipo_moneda_producto = req.POST.get("tipo_moneda_0")
        valor_producto = req.POST.get("valor_0")

        valido = True
        valido = valido and is_valid_text(titulo)
        valido = valido and is_valid_text(descripcion, 500)
        valido = valido and is_valid_text(video, 250)
        valido = valido and is_valid_text(categoria)
        #valido = valido and self.__is_valid(tiempo, 140) Falta determinar cantida max.
        #valido = valido and self.__is_valid(otros_productos) no se ni como llegara...
        #producto_0
        valido = valido and is_valid_text()

        creador_id = self.request.user.id

        if not valido:
            return common.Http500

        self.__guardar_proyecto(titulo, descripcion, creador_id, video, categoria, duracion)

        return redirect("nuevo_proyecto_paso_2")

    def __guardar_proyecto(self, titulo, descripcion, creador_id, video, categoria, duracion):
        tipo_proyecto_id = self.request.session.get("tipo_proyecto_id")

        proyecto = Proyecto()
        proyecto.titulo = titulo
        proyecto.descripcion = descripcion
        proyecto.creador = creador_id
        proyecto.video_url = video
        proyecto.duracion = duracion
        proyecto.tipo_proyecto = TipoProyecto.objects.get(pk = tipo_proyecto_id)
        proyecto.save()

        return proyecto.id

    def __guardar_producto(self, proyecto_id, nombre, desc, url, tipo_moneda, valor):
        pass


class NuevoProyecto2View(TemplateView):
    template_name = "nuevo_proyecto/nuevo_proyecto_paso_2.html"

class GuardarNuevoProyectoView(TemplateView):
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
        #valido = valido and self.__is_valid(tiempo, 140) Falta determinar cantida max.
        #valido = valido and self.__is_valid(otros_productos) no se ni como llegara...

        creador_id = self.request.user.id

        if not valido:
            return

        self.__guardar_proyecto(titulo, descripcion, creador_id, video, categoria, duracion)

    def __guardar_proyecto(self, titulo, descripcion, creador_id, video, categoria, duracion):
        tipo_proyecto_id = self.request.session.get("tipo_proyecto_id")

        proyecto = Proyecto()
        proyecto.titulo = titulo
        proyecto.descripcion = descripcion
        proyecto.creador = creador_id
        proyecto.video_url = video
        proyecto.duracion = duracion
        proyecto.tipo_proyecto = TipoProyecto.objects.get(pk = tipo_proyecto_id)
        proyecto.save()

        return proyecto.id


mis_proyectos = login_required(MisProyectosView.as_view())
nuevo_proyecto_paso_1 = login_required(NuevoProyecto1View.as_view())
guardar_paso_1 = login_required(GuardarPasoUno.as_view())
nuevo_proyecto_paso_2 = login_required(NuevoProyecto2View.as_view())
terminos_condiciones = login_required(TemplateView.as_view(template_name="dashboard/terminos_y_condiciones.html"))
tipo_proyecto = login_required(TemplateView.as_view(template_name="dashboard/tipo_de_proyecto.html"))
