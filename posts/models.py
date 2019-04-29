from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField(max_length=20, unique=True,help_text='Ja existe uma materia com esse titulo, Tente outro')
    assunto = models.CharField(max_length=20, blank=True, help_text='Digite o assunto a qual vc esta escrevendo!')
    materia = models.TextField(max_length=10000, unique=True, help_text='Escreva algo original!')
    data_de_postagem = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fonte = models.CharField(max_length=20, blank=True, help_text='Digite as suas fontes para não ter problemas de direito altoral')


    def __str__(self):
        return self.titulo


