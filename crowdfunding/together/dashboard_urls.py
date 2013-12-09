from django.conf.urls import patterns, url

urlpatterns = patterns('together.dashboard_views',
    url(r'^$', "dashboard", name="dashboard"),
    url(r'^mi\-perfil/', "mi_perfil", name="mi_perfil"),
)

urlpatterns += patterns("together.proyectos_view",
    url(r'^mis\-proyectos/', "mis_proyectos", name="mis_proyectos"),
    url(r'^terminos\-y\-condiciones/',"terminos_condiciones",name="terminos_condiciones"),
    url(r'^tipo\-de\-proyecto','tipo_proyecto',name="tipo_proyecto"),
    url(r'^nuevo\-proyecto/(\d+)/$',"nuevo_proyecto", name="nuevo_proyecto"),
    url(r'^guardar\-nuevo_proyecto/$',"guardar_nuevo_proyecto", name="guardar_nuevo_proyecto"),
)