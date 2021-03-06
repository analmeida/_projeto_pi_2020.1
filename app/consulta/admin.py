from django.contrib import admin
from consulta.models import *

class lista_consulta(admin.ModelAdmin):
    list_display = ('id','medico', 'atendente', 'paciente')
    list_display_links = ('medico', 'atendente', 'paciente')    

admin.site.register(Consulta, lista_consulta)