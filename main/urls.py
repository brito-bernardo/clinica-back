from django.urls import path
from main.views import PacienteView,RegisterRecepcionista, RegisterMedico, ProntuarioList, ProntuarioObjectView, LoginView, DiagnosticoCreateView, DiagnosticoList, CheckEmailView, ForgetPasswordView
urlpatterns = [
    path('pacientes/', PacienteView.as_view(), name='paciente-list'),
    path('prontuario/', ProntuarioList.as_view(), name='prontuario-list'),
    path('prontuario/<int:pk>/', ProntuarioObjectView.as_view(), name='prontuario-object'),
    path('prontuario/<int:pk>/diagnosticos/', DiagnosticoList.as_view(), name='diagnostico-list'),
    path('login/', LoginView.as_view(), name='login'),
    path('checkemail/', CheckEmailView.as_view(), name='checkemail'),
    path('forgetpassword/<int:pk>/', ForgetPasswordView.as_view(), name='forgetpassword'),
    path('diagnosticos/', DiagnosticoCreateView.as_view(), name='diagnostico-create'),
    path('cadastro-recepcionista/', RegisterRecepcionista.as_view(), name = 'cadastro-recepcionista'),
    path('cadastro-medico/', RegisterMedico.as_view(), name = 'cadastro-medico'),
    
]