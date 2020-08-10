"""mongo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from core import views as core_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.index,name="home"),
    path('gestor/', core_views.admnistrador, name="gestion"),
    path('gestor/lista_clientes', core_views.client, name="lista_clientes"),
    path('gestor/lista_reclamos', core_views.on_hold, name="lista_reclamos"),
    path('gestor/lista_reclamos/<slug:pk>', core_views.reclamo, name="rpta_ereclamo"),
    path('solicitudes/', core_views.solicitudes,name="solicitud"),
    path('reclamos', core_views.reclamos,name="reclamo"),
    path('gestor/lista_reclamos_respondido', core_views.reclamos_respondido,name="respondido"),
    path('gestor/lista_reclamos_excedido', core_views.reclamos_excedido,name="excedido"),
    path('gestor/lista_preguntas_reclamos', core_views.reclamos_questions,name="reclamos_questions"),
    path('gestor/planes', core_views.planess,name="planes"),
    path('login/', core_views.login.as_view(),name="login"),
    path('logout/', core_views.logout.as_view(),name="logout"),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
