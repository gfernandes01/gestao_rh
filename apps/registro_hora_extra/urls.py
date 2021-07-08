from django.urls import path
from .views import HoraExtraList


urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    # path('editar/<int:pk>/', FuncionariosEdit.as_view(), name='update_funcionarios'),
    # path('deletar/<int:pk>/', FuncionariosDelete.as_view(), name='delete_funcionarios'),
    # path('novo/', FuncionariosCreate.as_view(), name='create_funcionarios'),
]
# FuncionarioEdit, FuncionarioDelete, FuncionarioNovo