from django.db import models

class Cerveza(models.Model):
    marca = models.CharField(max_length = 60)
    color = models.CharField(max_length = 10)
    ibu = models.CharField(max_length = 5)
    alcohol = models.CharField(max_length = 4)
    cantMl = models.IntegerField()

    def __str__(self):
        return self.marca

class Ginebra(models.Model):
    marca = models.CharField(max_length = 60)
    sabor = models.CharField(max_length = 60)
    alcohol = models.CharField(max_length = 4)
    cantMl = models.IntegerField()

    def __str__(self):
        return self.marca


class Mezcal(models.Model):
    marca = models.CharField(max_length = 60)
    tipoAgave = models.CharField(max_length = 60)
    clasificacion = models.CharField(max_length = 20)
    alcohol = models.CharField(max_length = 4)
    cantMl = models.IntegerField()

    def __str__(self):
        return self.marca


