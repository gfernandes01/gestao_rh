from apps.registro_hora_extra.models import registroHoraExtra
from rest_framework import serializers


class registroHoraExtraSerializer(serializers.ModelSerializer):
	class Meta:
		model = registroHoraExtra
		fields = ('motivo', 'funcionario', 'horas', 'utilizada')
