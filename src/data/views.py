from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework.views import APIView
from .models import DataBatch


class ReceiveData(APIView):
    permission_classes = [IsAuthenticated]
    
    class serializer_class(serializers.Serializer):
        pass

    def post(self, request):
        """
        We only handle POST requests.

        Will return an empty HTTP 200 response if OK,
        HTTP 400 with an explanation if the request is invalid.

        """
        DataBatch.receive(request.user, request.data)
        return HttpResponse()
