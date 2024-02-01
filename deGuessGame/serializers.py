from rest_framework import serializers
from .models import DeWord


class DeWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeWord
        fields = '__all__'
