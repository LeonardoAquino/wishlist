from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.views.generic import TemplateView,ListView,View
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User

from ..models import Proyecto, TipoProyecto, Producto, Moneda
from ..models import Categoria, CuentaBancaria, TipoCuenta, Banco, DetalleUsuario
from ..common import is_text_valid, Http500, is_rut_valid

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
        template = "nuevo_proyecto/nuevo_proyecto_paso_1.html"

        data = {
            "dias" : [i + 1 for i in xrange(60)],
            "monedas" : Moneda.objects.all(),
            "categorias" : Categoria.objects.all(),
            "cantidad_impuesto" : 10
        }

        return render_to_response(template, data, context_instance=RequestContext(req))


class NuevoProyecto2View(TemplateView):
    template_name = "nuevo_proyecto/nuevo_proyecto_paso_2.html"
    def get_context_data(self, **kw):
        data = super(NuevoProyecto2View, self).get_context_data(**kw)
        data['bancos'] = Banco.objects.all()
        data['tipos_cuentas'] = TipoCuenta.objects.all()
        return data


class GuardarPasoUno(View):

    def post(self, req):

        titulo = req.POST.get('titulo')
        descripcion = req.POST.get('descripcion')
        video = req.POST.get('video')
        categoria = req.POST.get('categoria')
        duracion = req.POST.get('duracion')
        i = 0

        nombre_producto = req.POST.get("nombre_0")
        url_producto = req.POST.get("url_0")
        desc_producto = req.POST.get("descripcion_0")
        tipo_moneda_producto = req.POST.get("tipo_moneda_0")
        precio = req.POST.get("valor_0")

        valido = True
        valido = valido and is_text_valid(titulo)
        valido = valido and is_text_valid(descripcion, 500)
        valido = valido and is_text_valid(video, 250)

        productos_dict = []
        while True:
            if not is_text_valid(req.POST.get("nombre_%d"%i)):
                break

            nombre_producto = req.POST.get("nombre_%d"%i)
            url_producto = req.POST.get("url_%d"%i)
            desc_producto = req.POST.get("descripcion_%d"%i)
            tipo_moneda_producto = req.POST.get("tipo_moneda_%d"%i)
            precio = req.POST.get("valor_%d"%i)

            valido = valido and is_text_valid(nombre_producto)
            valido = valido and is_text_valid(url_producto, 500)
            valido = valido and is_text_valid(desc_producto, 500)
            valido = valido and is_text_valid(precio)
            #valido = valido and is_text_valid(tipo_moneda_producto)

            if not valido:
                break

            moneda = Moneda.objects.get(pk=1)
            prod = {
                "nombre": nombre_producto,
                "url": url_producto,
                "descripcion": desc_producto,
                "tipo_moneda_producto": moneda.id,
                "precio": precio,
            }

            productos_dict.append(prod)
            i += 1

        creador_id = self.request.user.id

        if not valido:
            raise Http500()

        proyecto_data ={
            "titulo": titulo,
            "descripcion": descripcion,
            "video": video,
            "categoria": categoria,
            "duracion": duracion,
            "creador_id":creador_id,
            "productos": productos_dict
        }

        req.session['f_nuevo_proyecto'] = proyecto_data
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

        return proyecto

    def __guardar_producto(self, items, proyecto):
        for item in items:
            producto = Producto()
            producto.nombre = item['nombre']
            producto.url = item['url']
            producto.precio = item['precio']
            producto.proyecto = proyecto
            producto.descripcion = item['descripcion']
            producto.moneda = item['tipo_moneda_producto']
            producto.save()

class GuardarPasoDos(View):
    def post(self,req):
        valido = True
        creador_id = self.request.user.id

        titular_cuenta = req.POST.get('titular_cuenta')
        num_cuenta = req.POST.get('num_cuenta')
        banco = req.POST.get('banco')
        rut = req.POST.get('rut')
        tipo_cuenta = req.POST.get('tipo_cuenta')

        valido = valido and is_text_valid(titular_cuenta)
        valido = valido and is_text_valid(num_cuenta)
        valido = valido and is_text_valid(banco)
        valido = valido and is_rut_valid(rut)
        valido = valido and is_text_valid(tipo_cuenta)

        if not valido:
            raise Http500()


        data_cuenta ={
            "titular": titular_cuenta,
            "cuenta": num_cuenta,
            "banco": banco,
            "rut": rut,
            "tipo": tipo_cuenta,
            "creador": creador_id
        }

        self.crear_cuenta(data_cuenta)
        return redirect("nuevo_proyecto_paso3")

    def crear_cuenta(self, data):
        try:
            cuenta = CuentaBancaria.objects.get(numero_cuenta = data['cuenta'])
        except cuenta.DoesNotExist as dne:
            banco = Banco.objects.get(pk=data['banco'])
            tipo_cuenta = TipoCuenta.objects.get(pk=data['tipo'])

            cuenta = CuentaBancaria()
            cuenta.numero_cuenta = data['cuenta']
            cuenta.tipo_cuenta = tipo_cuenta
            cuenta.banco = banco
            cuenta.save()

        try:
            detalle_usuario = DetalleUsuario.objects.get(usuario = data['creador'])
        except detalle_usuario.DoesNotExist as dne:
            creador = User.objects.get(pk=data['creador'])

            n_detalle = DetalleUsuario()
            n_detalle.usuario = creador
            n_detalle.rut = data['rut']
            n_detalle.cuenta_bancaria = cuenta
            n_detalle.save()

        return 1


class NuevoProyecto3View(TemplateView):
    template_name = "nuevo_proyecto/nuevo_proyecto_paso_3.html"



mis_proyectos = login_required(MisProyectosView.as_view())
nuevo_proyecto_paso1 = login_required(NuevoProyecto1View.as_view())
guardar_paso1 = login_required(GuardarPasoUno.as_view())
guardar_paso2 = login_required(GuardarPasoDos.as_view())
nuevo_proyecto_paso2 = login_required(NuevoProyecto2View.as_view())
nuevo_proyecto_paso3 = login_required(NuevoProyecto3View.as_view())
terminos_condiciones = login_required(TemplateView.as_view(template_name="nuevo_proyecto/terminos_y_condiciones.html"))
tipo_proyecto = login_required(TemplateView.as_view(template_name="nuevo_proyecto/tipo_de_proyecto.html"))

