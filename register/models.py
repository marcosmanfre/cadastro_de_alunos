from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=50, null=True, blank=True)
    sobrenome = models.CharField(max_length=50, null=True, blank=True)
    secao = models.CharField(max_length=50, null=True, blank=True)


def __str__(self):
    return self.Aluno
