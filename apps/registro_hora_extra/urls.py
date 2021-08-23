from django.urls import path

from .views import (
    HoraExtraList,
    HoraExtraEditBase,
    HoraExtraEdit,
    HoraExtraDelete,
    HoraExtraCreate,
    horaExtraUsada,
    horaExtraLivre,
    ExportarParaCSV,
    ExportarExcel,
)

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('editar-funcionario/<int:pk>/', HoraExtraEdit.as_view(), name='update_hora_extra'),
    path('editar/<int:pk>/', HoraExtraEditBase.as_view(), name='update_hora_extra_base'),
    path('hora-extra-usada/<int:pk>/', horaExtraUsada.as_view(), name='hora_extra_usada'),
    path('hora-extra-livre/<int:pk>/', horaExtraLivre.as_view(), name='hora_extra_livre'),
    path('deletar/<int:pk>/', HoraExtraDelete.as_view(), name='delete_hora_extra'),
    path('novo/', HoraExtraCreate.as_view(), name='create_hora_extra'),
    path('exportar-csv', ExportarParaCSV.as_view(), name='exportar_csv'),
    path('exportar-excel', ExportarExcel.as_view(), name='exportar_excel'),
]
