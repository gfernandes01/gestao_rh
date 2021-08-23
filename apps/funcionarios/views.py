import io
import xhtml2pdf.pisa as pisa

from django.template.loader import get_template
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from reportlab.pdfgen import canvas

from .models import Funcionario


class FuncionariosList(ListView):
	model = Funcionario

	def get_queryset(self):
		empresa_logada = self.request.user.funcionario.empresa
		return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionariosEdit(UpdateView):
	model = Funcionario
	fields = ['nome', 'departamentos']


class FuncionariosDelete(DeleteView):
	model = Funcionario
	success_url = reverse_lazy('list_funcionarios')


class FuncionariosCreate(CreateView):
	model = Funcionario
	fields = ['nome', 'departamentos']

	def form_valid(self, form):
		funcionario = form.save(commit=False)
		funcionario.empresa = self.request.user.funcionario.empresa
		funcionario.user = User.objects.create(
			username=funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1])
		funcionario.save()
		return super(FuncionariosCreate, self).form_valid(form)


def pdf_reportlab(request):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'  # Download PDF

	buffer = io.BytesIO()
	p = canvas.Canvas(buffer)

	p.drawString(200, 810, 'Relatório de funcionários')
	p.drawString(0, 800, '_' * 150)

	funcionarios = Funcionario.objects.filter(empresa=request.user.funcionario.empresa)

	str_ = 'Nome: %s -|- Hora Extra: %f'

	y = 780
	for funcionario in funcionarios:
		p.drawString(10, y, str_ % (funcionario.nome, funcionario.total_horas_extra))
		y -= 20

	p.showPage()
	p.save()

	pdf = buffer.getvalue()
	buffer.close()
	response.write(pdf)

	return response


class Render:

	@staticmethod
	def render(path: str, params: dict, filename: str):
		template = get_template(path)
		html = template.render(params)
		response = io.BytesIO()
		pdf = pisa.pisaDocument(
			io.BytesIO(html.encode("UTF-8")), response)
		if not pdf.err:
			response = HttpResponse(response.getvalue(), content_type='application/pdf')
			response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
			return response
		else:
			return HttpResponse("Error Rendering PDF", status=400)


class Pdf(View):

	def get(self, request):
		params = {
			'today': 'Variavel today',
			'sales': 'Variavel sales',
			'request': request,
		}
		return Render.render('funcionarios/relatorio.html', params, 'myfile')
