from rest_framework.generics import CreateAPIView
from . import serializers


class TokenView(CreateAPIView):
    serializer_class = serializers.TokenSerializer

