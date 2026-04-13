"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import include, path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='home'),
    
    path('cidade/', CidadeView.as_view()),
    path('ocupacao/', OcupacaoView.as_view()),
    path('pessoa/', PessoaView.as_view()),
    path('instituicao/', InstituicaoView.as_view()),
    path('curso/', CursoView.as_view()),
    path('disciplina/', DisciplinaView.as_view()),
    path('matricula/', MatriculaView.as_view()),
    path('avaliacao/', AvaliacaoView.as_view()),
    path('frequencia/', FrequenciaView.as_view()),
    path('ocorrencia/', OcorrenciaView.as_view()),
    path('area-saber/', AreaSaberView.as_view()),
    path('avaliacao-tipo/', AvaliacaoTipoView.as_view()),
    path('curso-disciplina/', CursoDisciplinaView.as_view()),
    path('turma/', TurmaView.as_view()),
    path('turnos/', TurnosView.as_view()),
]
