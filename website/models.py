from django.db import models

# Create your models here.


class Pessoa(models.Model):
    GENEROS = (
        ('MASCULINO', 'Masculino'),
        ('FEMININO', 'Feminino'),
        ('OUTROS', 'Outros')
    )

    nome = models.CharField(max_length=255, verbose_name='Nome')
    sobrenome = models.CharField(max_length=255, verbose_name='Sobrenome')
    genero = models.CharField(
        max_length=255, verbose_name='Gênero', choices=GENEROS)
    email = models.EmailField(
        max_length=255, verbose_name='Email', null=True, blank=True)
    data_de_criacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome + ' ' + self.sobrenome


class Ideia(models.Model):  # herdar as coisas do Django
    CATEGORIAS = (
        ('TERRA_PLANA', 'Terra Plana'),
        ('COACH', 'Coach'),
        ('PUBLICAS', 'Públicas'),
        ('OUTROS', 'Outros'),
    )

    pessoa = models.ForeignKey(
        Pessoa, on_delete=None
    )  # associar com outra tabela (deletou 1 deleta todas as asosciações da pessoa)

    titulo = models.CharField(
        max_length=255, verbose_name='Nome da Ideia', unique=True)
    descricao = models.TextField(verbose_name='Descreva sua ideia')


categorias = models.CharField(
    verbose_name='Categorias', choices=CATEGORIAS, max_length=255)
categoria_outros = models.CharField(
    null=True, blank=True, max_length=255, verbose_name='Outros, qual?')

data_de_criacao = models.DateTimeField(auto_now_add=True)
data_de_atualizacao = models.DateTimeField(auto_now=True)
ativo = models.BooleanField(default=True)
