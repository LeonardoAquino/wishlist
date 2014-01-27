from django.conf.urls import patterns, url

urlpatterns = patterns('together.pagos.views',
	url(r'^$', 'pago', name='pago'),
)
