from django.contrib import admin
from exames.models import *
# Register your models here.
class lista_exame_result(admin.ModelAdmin):
    list_display = ('paciente', 'data_exame', 'glicose', 'ldl', 'hdl','triglicerides', 'colesterol')
    list_display_links = ('data_exame', 'paciente') 

class lista_exame_ref(admin.ModelAdmin):
    list_display = ('id' ,'glicose_min', 'glicose_max', 'ldl_min', 'ldl_max', 'hdl_min', 'hdl_max', 'triglicerides_min', 'triglicerides_max','colesterol_min', 'colesterol_max', 'vldl_min', 'vldl_max','idade_min', 'idade_max')



admin.site.register(Exame_Resultado, lista_exame_result)
admin.site.register(Exame_Referencia, lista_exame_ref)