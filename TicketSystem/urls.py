from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tickets.urls')),  # Incluye las URLs de la aplicación tickets bajo el prefijo 'api/'
]


