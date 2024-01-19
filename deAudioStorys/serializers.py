from rest_framework import serializers
from .models import DeAudioStory


class DeAudioStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeAudioStory
        fields = '__all__'
