from django.db import models

class Vaga(models.Model):
    titulo    = models.CharField(max_length=200)
    descricao = models.TextField()
    salario   = models.DecimalField(max_digits=7,  decimal_places=2, null=False, blank=False)
