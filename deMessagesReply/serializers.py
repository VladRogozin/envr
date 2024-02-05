from rest_framework import serializers
from .models import DeMessagesReply


class DeMessagesReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeMessagesReply
        fields = '__all__'
