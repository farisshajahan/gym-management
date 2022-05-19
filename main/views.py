from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView

from main.serializers import TraineeSerializer, UserSerializer

User = get_user_model()

# Create your views here.
class SignUpView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user = super().post(request, *args, **kwargs)
        serializer = TraineeSerializer(data={"user": user.data["id"]})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return user
