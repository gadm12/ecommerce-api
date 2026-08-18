from django.shortcuts import render
from rest_framework.views import APIView
from .models import Client
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from .serializers import ClientSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class Sign_Up(APIView):
    def post(self, request):

        serializer = ClientSerializer(data=request.data)

        # new_user_data = request.data

        if serializer.is_valid():

            new_user = serializer.save()
            token = Token.objects.create(user=new_user)
            return Response(
                {
                    "client": new_user.email,
                    "token": token.key,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

        # new_user_inst = Client.objects.create_user(
        #     email=new_user_data.get("email"),
        #     password=new_user_data.get("password"),
        # )
        # token_inst = Token.objects.create(user=new_user_inst)
        # return Response(
        #     {
        #         "client": new_user_inst.email,
        #         "token": token_inst.key,
        #     },
        #     status=status.HTTP_201_CREATED,
        # )


class Log_in(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(
            request, email=email, password=password
        )
        if not user:
            return Response(
                "invalid email or password",
                status=status.HTTP_404_NOT_FOUND,
            )
        token, _ = Token.objects.get_or_create(user=user)

        return Response(
            {"client": user.email, "token": token.key},
            status=status.HTTP_200_OK,
        )


class ClientView(APIView):
    permission_classes = [IsAuthenticated]


class Log_out(ClientView):
    def post(self, request):
        user = request.data.get("email")
        request.user.auth_token.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )


class ClientInfo(ClientView):

    def get(self, request):
        user = request.user
        return Response(
            {
                "email": user.email,
            }
        )
