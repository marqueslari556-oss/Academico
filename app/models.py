from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")
    def __str__(self):
        return f'{self.nome}, {self.uf}'
    class Meta:
        verbose_name="Cidade"
        verbose_name_plural="Cidades"

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Ocupação da pessoa")
    def __str__(self):
        return f'{self.nome}'
    class Meta:
        verbose_name="Ocupação"
        verbose_name_plural="Ocupações"

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da pessoa")
    pai = models.CharField(max_length=100, verbose_name="Nome do pai")
    mãe = models.CharField(max_length=100, verbose_name="Nome da mãe")
    cpf = models.CharField(max_length=14, unique=True, verbose_name="Cpf da pessoa")
    data_nasc = models.DateField(verbose_name="Data de nascimento")
    email = models.CharField(max_length=100, verbose_name="Email")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade da pessoa")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name="Ocupação da Pessoa")
    def __str__(self):
        return f'{self.nome}, {self.email}'
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da instituição")
    site = models.CharField(max_lenght=100, verbose_name="Site da instituição")
    telefone = models.CharField(max_lenght=19, verbose_name="Telefone da instituição")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade da instituição")
    def __str__(self):
        return f'{self.nome}, {self.site}'
    class Meta:
        verbose_name="Instituição"
        verbose_name_plural="Instituições"

class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da área")
    def __str__(self):
        return f'{self.nome}'

class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do curso")
    carga_horaria_total = models.CharField(max_length=100, verbose_name="Carga horária do curso")
    duraao_meses = models.CharField(max_length=100, verbose_name="Duração do curso")
    def __str__(self):
        return f'{self.nome}'
    class Meta:
        verbose_name="Curso"
        verbose_name_plural="Cursos"

class Turma(models.Model):
    nome = models.CharField(max_length=100,verbose_name="Nome da turma")
    def __str__(self):
        return f'{self.nome}'
    class Meta:
        verbose_name="Turma"
        verbose_name_plural="Turmas"
    
class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da disciplina")
    AreaSaber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Nome da disciplina")
    def __str__(self):
        return f'{self.nome}'
    class Meta:
        verbose_name="Disciplina"
        verbose_name_plural="Disciplinas"

class Matricula(models.Model):
    InstituicaoEnsino = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Matrícula") 
    Curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Nome do curso")
    Pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Nome da Pessoa")    
    data_inicio = models.DateField(verbose_name="Data de inicio")
    data_previsao_termino = models.DateField(verbose_name="Data previsão de termino")
    def __str__(self):
        return f'{self.data_inicio}, {self.data_previsao_termino}'
    class Meta:
        verbose_name="Matríclula"
        verbose_name_plural="Matrículas"

class Avaliacao(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição")
    Curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Nome do curso")
    Disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Nome da disciplina")
    AvaliacaoTipo = models.ForeignKey(AvaliacaoTipo, on_delete=models.CASCADE, verbose_name="Tipo da avaliação")
    def __str__(self):
        return f'{self.descricao}, {self.AvaliacaoTipo}'
    class Meta:
        verbose_name="Avaliação"
        verbose_name_plural="Avaliações"

class Frequencia(models.Model):
    Curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Nome do curso")
    Disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Nome da disciplina")
    Pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Nome da pessoa")
    numero_faltas = models.IntegerField(verbose_name="Número de faltas")


