from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from emailapp.services import Email
from .models import email
from .serializers import UserSerializer
from rest_framework.renderers import TemplateHTMLRenderer


# Create your views here.
class EmailView(APIView):

    def get(self, request):
        email1 = email.objects.all()
        ser = UserSerializer(email1, many=True)
        return Response(ser.data)

    def post(self, request):
        status = Email.send(request.data)
        return Response({'message': status})
