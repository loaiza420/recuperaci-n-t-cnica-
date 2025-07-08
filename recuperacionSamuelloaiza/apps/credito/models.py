from django.db import models

# Create your models here.
class Credito(models.Model):
    Banco = models.TextField("Banco")
    Banco_id = models.TextField("Banco_id")
    valor = models.TextField("valor")