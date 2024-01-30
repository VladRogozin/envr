from rest_framework import generics
from .models import Spell
from .serializers import SpellSerializer


class SpellListView(generics.ListAPIView):
    serializer_class = SpellSerializer

    def get_queryset(self):
        amount = self.kwargs.get('amount', 10)

        queryset = Spell.objects.all()

        queryset = queryset.order_by('?')

        return queryset[:amount]


class SpellCreateView(generics.CreateAPIView):
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer
