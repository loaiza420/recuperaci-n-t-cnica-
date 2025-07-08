from django.db import models

# Create your models here.
class Banco(models.Model):
    cuenta = models.TextField("cuenta")
    rol_id = models.TextField("rol_id")
    transaccion = models.TextField("transaccion")