from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

