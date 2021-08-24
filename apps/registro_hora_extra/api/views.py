from rest_framework import viewsets
from apps.registro_hora_extra.api.serializers import registroHoraExtraSerializer
from apps.registro_hora_extra.models import registroHoraExtra
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class registroHoraExtraViewSet(viewsets.ModelViewSet):
	queryset = registroHoraExtra.objects.all()
	serializer_class = registroHoraExtraSerializer
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)

