from rest_framework import serializers
from .models import DeTextByEar


class DeTextByEarSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeTextByEar
        fields = '__all__'
