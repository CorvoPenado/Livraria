from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    nome_pessoa = models.CharField(max_length=100)
    dias_emprestimo = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nome_pessoa} - {self.livro.titulo}"

