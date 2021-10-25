from django.db import models
from django.utils import timezone

"""
CONTATOS
nome: STR * (obrigatório)
sobrenome: STR * (opcional)
telefone: STR * (obrigatório)
email: STR * (opcional)
data_criacao: DATETIME (automatic)
descricao: texto
categoria: CATEGORIA (other model)

CATEGORIA
nome: STR * (obrigatório)
"""


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30, blank=True)
    telefone = models.CharField(max_length=30)
    email = models.CharField(max_length=100, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
