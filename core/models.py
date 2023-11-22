from django.db import models

class Carro(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    anoFabricacao = models.IntegerField(null=True)
    potenciaCV = models.IntegerField(null=True)
    preco = models.FloatField(null=True)
    imgUrl = models.CharField(max_length=500)

    def __str__(self):
        if self.modelo:
            return self.modelo
        else:
            return "Carro sem modelo especificado"
