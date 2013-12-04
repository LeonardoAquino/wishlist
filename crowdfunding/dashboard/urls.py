from django.conf.urls import patterns, url

urlpatterns = patterns('dashboard.views',
    url(r'^$', "dashboard", name="dashboard"),
    url(r'^mis_proyectos/', "mis_proyectos", name="mis_proyectos"),
    url(r'^mi_perfil/', "mi_perfil", name="mi_perfil"),
    url(r'^nuevo_proyecto/$',"nuevo_proyecto", name="nuevo_proyecto"),
)
