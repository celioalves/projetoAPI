from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=40, blank=False, null=False)
    rg = models.CharField(max_length=9, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False, null=False)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

class CCurso(models.Model):
    
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    )
    
    codigo_curso = models.CharField(max_length=15)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.descricao
    

class Matricula(models.Model):

        PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno')
    )
        aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
        curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
        periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default='M')

