from apps.funcionarios.models import Funcionario
from rest_framework import serializers
from apps.registro_hora_extra.api.serializers import registroHoraExtraSerializer


class FuncionarioSerializer(serializers.ModelSerializer):
	registrohoraextra_set = registroHoraExtraSerializer(many=True)

	class Meta:
		model = Funcionario
		fields = ('id', 'nome', 'user', 'departamentos', 'empresa', 'total_horas_extra',
				  'registrohoraextra_set')
