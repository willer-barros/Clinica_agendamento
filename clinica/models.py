from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    celular = models.CharField(max_length=15, blank=False)
    idade = models.CharField(max_length=3, blank=False)

    def __str__(self):
        return self.nome, self.email, self.celular, self.idade


class Medico(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    celular = models.CharField(max_length=15, blank=False)
    especialidade = models.TextChoices("Cirurgião", "Especialista")


    def __str__(self):
        return self.nome


class Consulta(models.Model):
    paciente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()

    def __str__(self):
        return self.paciente, self.medico, self.data_hora