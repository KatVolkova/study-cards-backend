# study_cards/views.py

from rest_framework import viewsets, generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Flashcard
from .serializers import FlashcardSerializer
from .models import ReviewHistory
from .serializers import ReviewHistorySerializer

class FlashcardViewSet(viewsets.ModelViewSet):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['topic', 'status', 'next_review_date']

    def get_queryset(self):
        return Flashcard.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ReviewHistoryListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ReviewHistory.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
