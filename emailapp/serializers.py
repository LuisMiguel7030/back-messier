from emailapp.models import email
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = email
        fields = '__all__'
