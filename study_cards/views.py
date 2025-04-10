# study_cards/views.py

from rest_framework import viewsets, permissions
from .models import Flashcard
from .serializers import FlashcardSerializer


class FlashcardViewSet(viewsets.ModelViewSet):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer
    permission_classes = [permissions.IsAuthenticated]  

    def get_queryset(self):
        user = self.request.user
        return Flashcard.objects.filter(owner=user)


