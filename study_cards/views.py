# study_cards/views.py

from rest_framework import viewsets, permissions
from .models import Flashcard
from .serializers import FlashcardSerializer


class FlashcardViewSet(viewsets.ModelViewSet):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer
    permission_classes = [permissions.IsAuthenticated]  

    def get_queryset(self):
        return Flashcard.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


