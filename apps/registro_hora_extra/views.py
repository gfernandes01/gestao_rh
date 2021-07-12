from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import RegistroHoraExtraForm
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
	form_class = RegistroHoraExtraForm

	def get_form_kwargs(self):
		kwargs = super(HoraExtraEdit, self).get_form_kwargs()
		kwargs.update({'user': self.request.user})
		return kwargs


class HoraExtraDelete(DeleteView):
	model = registroHoraExtra
	success_url = reverse_lazy('list_hora_extra')


class HoraExtraCreate(CreateView):
	model = registroHoraExtra
	form_class = RegistroHoraExtraForm

	def get_form_kwargs(self):
		kwargs = super(HoraExtraCreate, self).get_form_kwargs()
		kwargs.update({'user': self.request.user})
		return kwargs
