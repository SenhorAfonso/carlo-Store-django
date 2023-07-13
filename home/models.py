from django.db import models

class Teste(models.Model):

    teste = models.IntegerField()

    def __str__(self):
        return self.teste