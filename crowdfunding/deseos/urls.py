from django.conf.urls import patterns, url

urlpatterns = patterns('deseos.views',
    url(r'^$','index', name="index"),
    url(r'^login/$','login',name="login"),
)