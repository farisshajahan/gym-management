from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView

from main.serializers import UserSerializer

User = get_user_model()

# Create your views here.
class SignUpView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
