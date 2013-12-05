from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crowdfunding.views.home', name='home'),
    # url(r'^crowdfunding/', include('crowdfunding.foo.urls')),
    url(r'^$',"deseos.views.index", name="index"),
    url(r'^login/$',"crowdfunding.views.login",name="login"),
    url(r'^logout/$',"crowdfunding.views.logout",name="logout"),
    url(r'^templates/.+?/$', 'crowdfunding.views.get_js_template', name="templates"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^registro/',include('registro.urls')),
)
