from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',"together.views.index", name="index"),
    url(r'^login/$',"together.views.login",name="login"),
    url(r'^logout/$',"together.views.logout",name="logout"),
    url(r'^templates/.+?/$', 'together.views.get_js_template', name="templates"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dashboard/', include('together.dashboard_urls')),
    url(r'^registro/',include('together.registro_urls')),
)
