from django.shortcuts import render
from .models import registroHoraExtra
from django.views.generic import ListView


# Create your views here.
class HoraExtraList(ListView):
	model = registroHoraExtra

	def get_queryset(self):
		empresa_logada = self.request.user.funcionario.empresa
		return registroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)
