
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FlashcardViewSet
from .views import ReviewHistoryListCreateView

router = DefaultRouter()
router.register(r'flashcards', FlashcardViewSet, basename='flashcard')

urlpatterns = [
    path('', include(router.urls)),
    path('review-history/', ReviewHistoryListCreateView.as_view(), name='review-history'),
]
