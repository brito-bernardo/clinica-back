from django.db import models
from django.contrib.auth.models import User
from main.constantes import *
# Create your models here.

class UserBasic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class Meta:
        abstract = True
    def __str__(self):
        return self.user.username

class Paciente(UserBasic):
    pass

class Medico(UserBasic):
    especialidade = models.CharField(max_length=100, default='clinico geral')

class Recepcionista(UserBasic):
    pass

class Prontuario(models.Model):
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    birthday = models.DateField()
    sex = models.CharField(max_length=1, choices=SEXCHOICES)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    description = models.TextField()
    allergies = models.TextField()

class Diagnostico(models.Model):
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE, related_name='diagnosticos')
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
