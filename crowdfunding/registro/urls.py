from django.conf.urls import patterns, include, url

urlpatterns = patterns('registro.views',
    url(r'^$', 'registro', name='registro'),
    url(r'^obtener_comunas/','obtener_comunas', name="obtener_comunas"),
    url(r'^verificar_usuario/',"verificar_usuario", name="verificar_usuario"),
    url(r'^envio/', "envio", name="envio"),
)
