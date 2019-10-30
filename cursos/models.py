from django.db import models

class Cursos(models.Model):
    nome = models.CharField(max_length=255)
    carga_horaria = models.IntegerField()
    ementa = models.CharField(max_length=255)
    valor = models.FloatField()

    def __str__(self):
        return self.nome