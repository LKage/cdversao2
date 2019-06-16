from django.db import models


# Create your models here.

class PessoaModel(models.Model):
    pessoa_id = models.AutoField(primary_key=True)
    pessoa_nome = models.CharField(
        max_length=100,
        default="",
        null=False,
        blank=False,
        verbose_name="Nome")
    estado_nome = models.CharField(
        max_length=100,
        default="",
        null=False,
        blank=False,
        verbose_name="Logradouro")
    cidade_nome = models.CharField(
        max_length=100,
        default="",
        null=False,
        blank=False,
        verbose_name="Logradouro")
    pessoa_logradouro = models.CharField(
        max_length=100,
        default="",
        null=False,
        blank=False,
        verbose_name="Logradouro")
    pessoa_numero = models.CharField(
        max_length=5,
        default="",
        null=False,
        blank=False,
        verbose_name="Número")
    # c = ContatoModel(
    contato_telefone = models.CharField(
        max_length=5,
        default="",
        null=False,
        blank=False,
        verbose_name="Telefone")

    class Meta:
        ordering = ['pessoa_nome']
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    def __str__(self):
        return self.pessoa_nome


class ContatoModel(models.Model):
    contato_id = models.AutoField(primary_key=True)
    contato_telefone = models.CharField(
        max_length=15,
        default="",
        null=False,
        blank=False,
        verbose_name="Telefone")
    pessoa = models.ForeignKey(PessoaModel, on_delete=models.CASCADE)

    class Meta:
        ordering = ['contato_id']
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.contatos


class EstadoModel(models.Model):
    estado_id = models.AutoField(primary_key=models.CASCADE)
    estado_nome = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Estado")
    # pessoa_nome = models.OneToOneField(PessoaModel, null=True, blank=True, on_delete=CASCADE)


class Meta:
    ordering = ['estado_id']
    verbose_name = 'Estado'
    verbose_name_plural = 'Estados'


def __str__(self):
    return self.estado


class CidadeModel(models.Model):
    estado_id = models.ForeignKey(PessoaModel, null=True, blank=True, on_delete=models.CASCADE)
    cidade_nome = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Cidade")


class Meta:
    ordering = ['cidade_id']
    verbose_name = 'Cidade'
    verbose_name_plural = 'Cidades'


def __str__(self):
    return self.cidade
