
from rest_framework import serializers
from .models import Flashcard
from .models import ReviewHistory


class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = '__all__'
        read_only_fields = ['owner', 'created_at', 'updated_at', 'next_review_date']


class ReviewHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewHistory
        fields = ['id', 'user', 'date', 'correct', 'total', 'score', 'streak']
        read_only_fields = ['user', 'date']