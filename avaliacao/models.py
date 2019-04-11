from django.db import models
from django.contrib.auth.models import User


class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField(null=True, blank=True)
    nota = models.DecimalField(max_digits=3, decimal_places=1)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.username

    class Meta:
        verbose_name_plural = 'Avaliacoes'