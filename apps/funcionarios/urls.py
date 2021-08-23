from django.urls import path
from .views import(
    FuncionariosList,
    FuncionariosEdit,
    FuncionariosDelete,
    FuncionariosCreate,
    pdf_reportlab,
    Pdf,
)

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>/', FuncionariosEdit.as_view(), name='update_funcionarios'),
    path('deletar/<int:pk>/', FuncionariosDelete.as_view(), name='delete_funcionarios'),
    path('novo/', FuncionariosCreate.as_view(), name='create_funcionarios'),
    path('pdf-reportlab/', pdf_reportlab, name='pdf_reportlab'),
    path('relatorio_funcionarios_html', Pdf.as_view(), name='relatorio_funcionarios_html'),
]
