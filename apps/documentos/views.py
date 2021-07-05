from django.urls import reverse
from django.views.generic import CreateView
from .models import Documento


# Create your views here.
class DocumentoCreate(CreateView):
	model = Documento
	fields = ['descricao', 'documento']

	def post(self, request, *args, **kwargs):
		form = self.get_form()
		form.instance.pertence_id = self.kwargs['funcionario_id']

		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def get_success_url(self):
		return reverse('update_funcionarios', args=[self.kwargs['funcionario_id']])
