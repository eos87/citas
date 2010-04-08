from django.conf.urls.defaults import *
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'citas.control.views.ver_dia'),    
    (r'^editar/(?P<id>\w+)/$', 'citas.control.views.editar'),
    (r'^agregar/$', 'citas.control.views.nueva_cita'),
    (r'^borrar/$', 'citas.control.views.borrar'),
    (r'^cambiar_fechas/$', 'citas.control.views.cambiar_fechas'),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.PROJECT_DIR + '/files'}),
)
