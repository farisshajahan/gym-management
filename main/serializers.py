from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from main.models import Programme, Trainee

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "address",
            "email",
            "password",
            "date_of_birth",
            "phone",
        ]

    def validate_password(self, value: str) -> str:
        return make_password(value)

    def to_representation(self, obj):
        repr = super(UserSerializer, self).to_representation(obj)
        repr.pop("password")
        return repr


class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainee
        fields = "__all__"


class ProgrammeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programme
        fields = ["name", "fee", "duration"]
