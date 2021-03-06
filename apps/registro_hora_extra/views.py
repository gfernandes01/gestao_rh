import csv
import json

import xlwt
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

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


class HoraExtraEditBase(UpdateView):
	model = registroHoraExtra
	form_class = RegistroHoraExtraForm
	success_url = reverse_lazy('list_hora_extra')

	def get_form_kwargs(self):
		kwargs = super(HoraExtraEditBase, self).get_form_kwargs()
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


class horaExtraUsada(View):
	def post(self, *args, **kwargs):
		registro_hora_extra = registroHoraExtra.objects.get(id=kwargs['pk'])
		registro_hora_extra.utilizada = True
		registro_hora_extra.save()
		empregado = self.request.user.funcionario

		response = json.dumps(
			{'mensagem': 'Requisição executada', 'horas': float(empregado.total_horas_extra)}
		)

		return HttpResponse(response, content_type='application/json')


class horaExtraLivre(View):
	def post(self, *args, **kwargs):
		registro_hora_extra = registroHoraExtra.objects.get(id=kwargs['pk'])
		registro_hora_extra.utilizada = False
		registro_hora_extra.save()
		empregado = self.request.user.funcionario

		response = json.dumps(
			{'mensagem': 'Requisição executada', 'horas': float(empregado.total_horas_extra)}
		)

		return HttpResponse(response, content_type='application/json')


class ExportarParaCSV(View):
	def get(self, request):
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

		registro_horas = registroHoraExtra.objects.filter(utilizada=False)

		writer = csv.writer(response)
		writer.writerow(['Id', 'Motivo', 'Funcionario', 'Rest. Func', 'Horas'])

		for registro in registro_horas:
			writer.writerow(
				[registro.id, registro.motivo, registro.funcionario,
				 registro.funcionario.total_horas_extra, registro.horas
				 ])

		return response


class ExportarExcel(View):
	def get(self, request):
		response = HttpResponse(content_type='application/ms-excel')
		response['Content-Disposition'] = 'attachment; filename="relatorio_excel.xls"'

		wb = xlwt.Workbook(encoding='utf-8')
		ws = wb.add_sheet('Users')

		row_num = 0

		font_style = xlwt.XFStyle()
		font_style.font.bold = True

		columns = ['Id', 'Motivo', 'Funcionario', 'Rest. Func', 'Horas']

		for col_num in range(len(columns)):
			ws.write(row_num, col_num, columns[col_num], font_style)

		font_style = xlwt.XFStyle()

		registros = registroHoraExtra.objects.filter(utilizada=False)

		row_num = 1
		for registro in registros:
			ws.write(row_num, 0, registro.id, font_style)
			ws.write(row_num, 1, registro.motivo, font_style)
			ws.write(row_num, 2, registro.funcionario.nome, font_style)
			ws.write(row_num, 3, registro.funcionario.total_horas_extra, font_style)
			ws.write(row_num, 4, registro.horas, font_style)
			row_num += 1

		wb.save(response)
		return response