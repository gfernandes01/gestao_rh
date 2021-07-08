from django.shortcuts import render
from django.urls import reverse_lazy

from .models import registroHoraExtra
from django.views.generic import ListView, UpdateView, DeleteView, CreateView


# Create your views here.
class HoraExtraList(ListView):
	model = registroHoraExtra

	def get_queryset(self):
		empresa_logada = self.request.user.funcionario.empresa
		return registroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class HoraExtraEdit(UpdateView):
	model = registroHoraExtra
	fields = ['motivo', 'funcionario', 'horas']


class HoraExtraDelete(DeleteView):
	model = registroHoraExtra
	success_url = reverse_lazy('list_hora_extra')


class HoraExtraCreate(CreateView):
	model = registroHoraExtra
	fields = ['motivo', 'funcionario', 'horas']