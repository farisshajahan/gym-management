from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from main.models import Programme, Trainer, TrainerProgramme
from main.permissions import IsSuperUser, ReadOnly
from main.serializers import (
    ProgrammeSerializer,
    TrainerSerializer,
    UserCreateSerializer,
)


class TrainerViewset(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    permission_classes = [IsSuperUser | (IsAdminUser & ReadOnly)]

    def create(self, request, *args, **kwargs):
        if "basic_salary" not in request.data:
            return Response({"basic_salary": ["this field is required"]}, HTTP_400_BAD_REQUEST)
        user_serializer = UserCreateSerializer(data={**request.data, "is_staff": True})
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        trainer_serializer = TrainerSerializer(data={**request.data, "user": user_serializer.data["id"]})
        trainer_serializer.is_valid(raise_exception=True)
        trainer_serializer.save()
        return Response(
            {
                **trainer_serializer.data,
                "user": user_serializer.data,
            },
            HTTP_201_CREATED,
        )


class ProgrammeViewset(viewsets.ModelViewSet):
    queryset = Programme.objects.all()
    serializer_class = ProgrammeSerializer
    permission_classes = [(IsAuthenticated & IsAdminUser) | ReadOnly]

    @action(detail=True, methods=["post"])
    def add_trainer(self, request, pk=None):
        programme = self.get_object()
        trainer = Trainer.objects.get(pk=int(request.data["trainer_id"]))
        TrainerProgramme(
            trainer=trainer,
            programme=programme,
            commission=int(request.data["commission"]),
        ).save()
        return Response(None, HTTP_200_OK)
