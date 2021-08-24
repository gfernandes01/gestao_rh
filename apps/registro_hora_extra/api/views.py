from rest_framework import viewsets
from apps.registro_hora_extra.api.serializers import registroHoraExtraSerializer
from apps.registro_hora_extra.models import registroHoraExtra


class registroHoraExtraViewSet(viewsets.ModelViewSet):
	queryset = registroHoraExtra.objects.all()
	serializer_class = registroHoraExtraSerializer
