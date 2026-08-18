from rest_framework.serializers import ModelSerializer

from .models import Client


class ClientSerializer(ModelSerializer):
    class Meta:

        model = Client
        fields = ["id", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return Client.objects.create_user(**validated_data)
