from rest_framework import serializers
from .models import EnAudioStory


class EnAudioStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EnAudioStory
        fields = '__all__'
