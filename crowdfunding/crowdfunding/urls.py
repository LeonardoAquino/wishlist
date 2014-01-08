from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('together.views',
    url(r'^$',"index", name="index"),
    url(r'^ingresar/$',"ingresar", name="ingresar"),
    url(r'^login/$',"login",name="login"),
    url(r'^fb_login/$',"fb_login",name="login"),
    url(r'^logout/$',"logout",name="logout"),
    url(r'^templates/.+?/$', 'get_js_template', name="templates"),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dashboard/', include('together.dashboard.urls')),
    url(r'^registro/',include('together.registro.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
