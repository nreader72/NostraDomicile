from django.conf.urls import url
from NostraDomicile import views, settings
from django.conf.urls.static import static
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^test.html', views.test, name='test'),
]

#urlpatterns += patterns('django.views.static',
#        (r'^%s(?P<path>.*)' % settings.STATIC_URL, 'serve',
#         {'document_root': settings.STATIC_ROOT}))

#urlpatterns += staticfiles_urlpatterns()
