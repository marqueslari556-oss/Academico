from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    
class CidadeView(View):
    def get(self, request):
        cidades = Cidade.objects.all()
        return render(request, 'Cidade.html', {'cidades': cidades})


class OcupacaoView(View):
    def get(self, request):
        ocupacoes = Ocupacao.objects.all()
        return render(request, 'Ocupacao.html', {'ocupacoes': ocupacoes})

class PessoaView(View):
    def get(self, request):
        pessoas = Pessoa.objects.all()
        return render(request, 'Pessoa.html', {'pessoas': pessoas})

class InstituicaoView(View):
    def get(self, request):
        instituicoes = InstituicaoEnsino.objects.all()
        return render(request, 'InstituicaoEnsino.html', {'instituicoes': instituicoes})

class CursoView(View):
    def get(self, request):
        cursos = Curso.objects.all()
        return render(request, 'Curso.html', {'cursos': cursos})

class DisciplinaView(View):
    def get(self, request):
        disciplinas = Disciplina.objects.all()
        return render(request, 'Disciplina.html', {'disciplinas': disciplinas})

class MatriculaView(View):
    def get(self, request):
        matriculas = Matricula.objects.all()
        return render(request, 'Matricula.html', {'matriculas': matriculas})

class AvaliacaoView(View):
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        return render(request, 'Avaliacao.html', {'avaliacoes': avaliacoes})

class FrequenciaView(View):
    def get(self, request):
        frequencias = Frequencia.objects.all()
        return render(request, 'Frequencia.html', {'frequencias': frequencias})


class OcorrenciaView(View):
    def get(self, request):
        ocorrencias = Ocorrencia.objects.all()
        return render(request, 'Ocorrencia.html', {'ocorrencias': ocorrencias})


class AreaSaberView(View):
    def get(self, request):
        areas = AreaSaber.objects.all()
        return render(request, 'AreaSaber.html', {'areas': areas})


class AvaliacaoTipoView(View):
    def get(self, request):
        tipos = AvaliacaoTipo.objects.all()
        return render(request, 'AvaliacaoTipo.html', {'tipos': tipos})


class CursoDisciplinaView(View):
    def get(self, request):
        cursos_disciplinas = CursoDisciplina.objects.all()
        return render(request, 'CursoDisciplina.html', {'cursos_disciplinas': cursos_disciplinas})


class TurmaView(View):
    def get(self, request):
        turmas = Turma.objects.all()
        return render(request, 'Turma.html', {'turmas': turmas})


class TurnosView(View):
    def get(self, request):
        turnos = Turnos.objects.all()
        return render(request, 'Turnos.html', {'turnos': turnos})