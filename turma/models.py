from django.db import models

class Turma(models.Model):
    data_inicio = models.DateTimeField()
    data_termino = models.DateTimeField()
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()

    def __str__(self):
        return self.data_inicio
