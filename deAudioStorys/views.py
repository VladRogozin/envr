from rest_framework import generics
from .models import DeAudioStory
from .serializers import DeAudioStorySerializer


class DeAudioStoryListView(generics.ListAPIView):
    serializer_class = DeAudioStorySerializer

    def get_queryset(self):
        amount = self.kwargs.get('amount', 10)

        queryset = DeAudioStory.objects.all()

        queryset = queryset.order_by('?')

        return queryset[:amount]


class DeAudioStoryCreateView(generics.CreateAPIView):
    queryset = DeAudioStory.objects.all()
    serializer_class = DeAudioStorySerializer
