from django.db import models

# Create your models here.
class Debito(models.Model):
    Banco = models.TextField("Banco")
    valor = models.TextField("valor")