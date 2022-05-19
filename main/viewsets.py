from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from main.models import Programme
from main.permissions import ReadOnly
from main.serializers import ProgrammeSerializer


class ProgrammeViewset(viewsets.ModelViewSet):
    queryset = Programme.objects.all()
    serializer_class = ProgrammeSerializer
    permission_classes = [(IsAuthenticated & IsAdminUser) | ReadOnly]
