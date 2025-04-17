from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Flashcard(models.Model):
    # The owner of the flashcard
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="flashcards")
    
    # Fields to store content
    question = models.TextField()
    answer = models.TextField()
    topic = models.CharField(max_length=100, blank=True, null=True)

    # Status field: "new", "reviewing", "mastered" (default "new")
    status = models.CharField(
        max_length=20, choices=[('new', 'New'), ('reviewing', 'Reviewing'), ('mastered', 'Mastered')],
        default='new'
    )
    
    # Timestamps
    next_review_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.owner.username} - {self.topic or 'General'}"


class ReviewHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review_sessions")
    date = models.DateTimeField(auto_now_add=True)
    correct = models.IntegerField()
    total = models.IntegerField()
    score = models.DecimalField(max_digits=5, decimal_places=2)
    streak = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.user.username} - {self.date.strftime('%Y-%m-%d %H:%M:%S')} - {self.score}%"