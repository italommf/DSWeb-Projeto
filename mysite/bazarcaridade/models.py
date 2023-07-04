from django.db import models
from django.utils import timezone


class Evento(models.Model):
    nome_evento = models.CharField(max_length=50, null=False, default='')
    data_inicio = models.DateField(default=timezone.now)
    data_fim = models.DateField(null=True, blank=True)
    descricao_evento = models.TextField(max_length=255, null=True)

    def __str__(self):
        return f"Evento: {self.nome_evento} - Início: {self.data_inicio} - Fim: {self.data_fim}"


class Item(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, default=1)
    nome_item = models.CharField(max_length=50, null=False, default='')
    descricao_item = models.CharField(max_length=255, null=True)
    preco = models.IntegerField(default=0, null=False)
    upload = models.ImageField(null=False, upload_to='uploads/')

    def __str__(self):
        return f"{self.nome_item}"


class Usuario(models.Model):
    ...
