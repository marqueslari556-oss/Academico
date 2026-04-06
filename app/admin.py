from django.contrib import admin
from .models import *

class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    inlines = [PessoaInline]

class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

class InstituicaoEnsinoAdmin(admin.ModelAdmin):
    inlines = [CursoInline]

admin.site.register(Cidade)
admin.site.register(Ocupacao, OcupacaoAdmin)
admin.site.register(Pessoa)
admin.site.register(InstituicaoEnsino, InstituicaoEnsinoAdmin)
admin.site.register(Curso)
admin.site.register(AreaSaber)
admin.site.register(Turma)
admin.site.register(Disciplina)
admin.site.register(Matricula)
admin.site.register(AvaliacaoTipo)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(Turnos)
admin.site.register(Ocorrencia)
admin.site.register(CursoDisciplina)

