from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuario.urls')),
    path('pacientes/', include('paciente.urls')),
    path('consulta/', include('consulta.urls')),
    path('exames/', include('exames.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)