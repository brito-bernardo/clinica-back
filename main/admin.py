from django.contrib import admin
from main.models import Paciente, Medico, Recepcionista, Prontuario, Diagnostico

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Recepcionista)
admin.site.register(Prontuario)
admin.site.register(Diagnostico)