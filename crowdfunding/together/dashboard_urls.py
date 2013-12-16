from django.conf.urls import include, patterns, url

urlpatterns = patterns('together.dashboard_views',
    url(r'^$', "dashboard", name="dashboard"),
    url(r'^mi\-perfil/', "mi_perfil", name="mi_perfil"),
    url(r'^proyecto_detalle/(\d+)', "ver_proyecto", name="ver_proyecto"),
)

urlpatterns += patterns("together.proyectos_view",
    url(r'^mis\-proyectos/', "mis_proyectos", name="mis_proyectos"),
    url(r'^nuevo\-proyecto/',include("together.nuevo_proyecto_urls")),
)
