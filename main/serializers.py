from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from main.models import Programme, Trainee, Trainer

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

    def validate_password(self, value):
        return make_password(value)

    def to_representation(self, obj):
        repr = super(UserSerializer, self).to_representation(obj)
        repr.pop("password")
        return repr


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def validate_password(self, value):
        return make_password(value)

    def to_representation(self, obj):
        repr = super(UserCreateSerializer, self).to_representation(obj)
        repr.pop("password")
        return repr


class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainee
        fields = "__all__"


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = "__all__"


class TrainerCreateSerializer(serializers.ModelSerializer):
    basic_salary = serializers.IntegerField()

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


class ProgrammeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programme
        fields = ["id", "name", "fee", "duration"]
