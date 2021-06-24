from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Departamento
from ..funcionarios.models import Funcionario


# Create your views here.

class DepartamentosList(ListView):
	model = Departamento

	def get_queryset(self):
		empresa_logada = self.request.user.funcionario.empresa
		return Departamento.objects.filter(empresa=empresa_logada)


class DepartamentosCreate(CreateView):
	model = Departamento
	fields = ['nome']

	def form_valid(self, form):
		departamento = form.save(commit=False)
		departamento.empresa = self.request.user.funcionario.empresa
		departamento.save()
		return super(DepartamentosCreate, self).form_valid(form)


class DepartamentosEdit(UpdateView):
	model = Departamento
	fields = ['nome']


class DepartamentosDelete(DeleteView):
	model = Departamento
	success_url = reverse_lazy('list_departamentos')
