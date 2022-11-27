from django.contrib.auth.models import AbstractUser
from django.db import models


class FinancialMovement(models.Model):
    tipo = models.IntegerField()
    data = models.CharField(max_length=8)
    valor = models.CharField(max_length=10)
    CPF = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora= models.CharField(max_length=6)
    dono = models.CharField(max_length=14)
    loja = models.CharField(max_length=19)
    uploaded_file = models.FileField(upload_to = "uploaded_file/")



