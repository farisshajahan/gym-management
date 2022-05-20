import time

import jwt
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from main.cache import cache
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


class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        access_token = None
        if "Authorization" in request.headers and "Bearer" in request.headers["Authorization"]:
            access_token = request.headers["Authorization"].split()[1]
            token_payload = jwt.decode(access_token, options={"verify_signature": False})
            cache.add_key(access_token, "1")
            cache.set_ttl(access_token, int(token_payload["exp"]) - int(time.time()))
        return Response(None, HTTP_200_OK)
