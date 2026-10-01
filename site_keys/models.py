from django.db import models

class Key(models.Model):
    titulo = models.CharField(max_length=200)
    plataforma = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    preco_anterior = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    descricao = models.TextField()
    imagem_url = models.URLField(max_length=500, blank=True)
    estoque = models.PositiveIntegerField(default=0)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo