from django.urls import path
from .views import FuncionariosList,\
    FuncionariosEdit,\
    FuncionariosDelete,\
    FuncionariosCreate


urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>/', FuncionariosEdit.as_view(), name='update_funcionarios'),
    path('deletar/<int:pk>/', FuncionariosDelete.as_view(), name='delete_funcionarios'),
    path('novo/', FuncionariosCreate.as_view(), name='create_funcionarios'),
]
