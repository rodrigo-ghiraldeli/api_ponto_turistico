"""ponto_turistico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static

from core.api.viewssets import PontoTuristicoViewSet
from atracao.api.viewssets import AtracaoViewSet
from endereco.api.viewssets import EnderecoViewSet
from comentario.api.viewssets import ComentarioViewSet
from avaliacao.api.viewssets import AvaliacaoViewSet

router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet,
                basename='PontoTuristico')
router.register(r'atracao', AtracaoViewSet)
router.register(r'endereco', EnderecoViewSet)
router.register(r'comentario', ComentarioViewSet)
router.register(r'avaliacao', AvaliacaoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
