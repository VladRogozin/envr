from rest_framework import generics
from .models import EnAudioStory
from .serializers import EnAudioStorySerializer


class EnAudioStoryListView(generics.ListAPIView):
    serializer_class = EnAudioStorySerializer

    def get_queryset(self):
        amount = self.kwargs.get('amount', 10)

        queryset = EnAudioStory.objects.all()

        queryset = queryset.order_by('?')

        return queryset[:amount]


class EnAudioStoryCreateView(generics.CreateAPIView):
    queryset = EnAudioStory.objects.all()
    serializer_class = EnAudioStorySerializer
