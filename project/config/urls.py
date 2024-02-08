
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(("core.urls","core"))),
    path("cliente/", include(("cliente.urls", "cliente"))),
    path("rutinas/", include(("rutina.urls", "rutina"))),
]
