from django.db import models
from django.contrib.auth.models import User

class Produtos(models.Model):
    name = models.CharField(max_length = 50, null = False, primary_key = True)
    quant = models.IntegerField(default = 0, null = False)
    descPro = models.CharField(max_length = 255, null = False)
    price = models.FloatField(default = 0, null = False)

    def __str__(self) -> str:
        return self.name

class Entrada(models.Model):
    name = models.ForeignKey(Produtos, on_delete = models.DO_NOTHING)
    quant = models.IntegerField(default = 0, null = False)
    descEnt = models.CharField(max_length = 255, null = False)
    price = models.FloatField(default = 0, null = False)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    regis_por = models.ForeignKey(User, on_delete = models.DO_NOTHING)

class Saida(models.Model):
    name = models.ForeignKey(Produtos, on_delete = models.DO_NOTHING)
    quant = models.IntegerField(default = 0, null = False)
    descSai = models.CharField(max_length = 255, null = False)
    price = models.FloatField(default = 0, null = False)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    regis_por = models.ForeignKey(User, on_delete = models.DO_NOTHING, default = User)
    

