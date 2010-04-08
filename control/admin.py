from citas.control.models import *
from django.contrib import admin

admin.site.register(Citas,
	list_display = ['cliente', 'hora_ini', 'hora_fin', 'fecha'],
	list_filter = ['cliente', 'hora_ini', 'hora_fin', 'fecha'],
	ordering = ['cliente', 'fecha'],
	search_fields = ['cliente', 'trabajo_realizar'],	
)
