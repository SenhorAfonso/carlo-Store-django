from django.db import models

class EcommerceImages(models.Model):

    id = models.IntegerField(primary_key=True)
    imagem = models.ImageField(upload_to = 'ecommerce_imgs')

    def __str__(self):
        return self.id
