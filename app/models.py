from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f'{self.nome}, {self.uf}'

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Ocupação da pessoa")

    def __str__(self):
        return f'{self.nome}'

    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"


class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da pessoa")
    pai = models.CharField(max_length=100, verbose_name="Nome do pai")
    mae = models.CharField(max_length=100, verbose_name="Nome da mãe")
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF")
    data_nasc = models.DateField(verbose_name="Data de nascimento")
    email = models.CharField(max_length=100, verbose_name="Email")

    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name="Ocupação")

    def __str__(self):
        return f'{self.nome}, {self.email}'

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"


class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da instituição")
    site = models.CharField(max_length=100, verbose_name="Site")
    telefone = models.CharField(max_length=19, verbose_name="Telefone")

    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")

    def __str__(self):
        return f'{self.nome}'

    class Meta:
        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"


class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Área")

    def __str__(self):
        return f'{self.nome}'

    class Meta:
        verbose_name = "Área"
        verbose_name_plural = "Áreas"


class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Curso")
    carga_horaria_total = models.IntegerField(verbose_name="Carga horária")
    duracao_meses = models.IntegerField(verbose_name="Duração (meses)")

    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome}'

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"


class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Turma")

    def __str__(self):
        return f'{self.nome}'

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"


class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Disciplina")

    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome}'

    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"


class Matricula(models.Model):
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    data_inicio = models.DateField(verbose_name="Data de início")
    data_previsao_termino = models.DateField(verbose_name="Previsão de término")

    def __str__(self):
        return f'{self.pessoa} - {self.curso}'

    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"


class AvaliacaoTipo(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Tipo de avaliação")

    def __str__(self):
        return f'{self.nome}'

    class Meta:
        verbose_name = "Tipo de avaliação"


class Avaliacao(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição")

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    avaliacao_tipo = models.ForeignKey(AvaliacaoTipo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.descricao}'

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"


class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    numero_faltas = models.IntegerField(verbose_name="Faltas")

    def __str__(self):
        return f'{self.numero_faltas}'

    class Meta:
        verbose_name = "Frequência"


class Turnos(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Turno")

    def __str__(self):
        return f'{self.nome}'

    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"


class Ocorrencia(models.Model):
    descricao = models.CharField(max_length=100)
    data = models.DateField()

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pessoa} - {self.curso}'

    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"


class CursoDisciplina(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    carga_horaria = models.IntegerField()
    periodo = models.CharField(max_length=2, verbose_name="Período")

    def __str__(self):
        return f'{self.curso} - {self.disciplina}'

    class Meta:
        verbose_name = "Curso Disciplina"
        verbose_name_plural = "Cursos Disciplinas"