from django.db import models
from django.contrib.auth.models import User


class Flashcard(models.Model):
    # The owner of the flashcard
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="flashcards")
    
    # Fields to store content
    question = models.TextField()
    answer = models.TextField()
    topic = models.CharField(max_length=100, blank=True, null=True)
    
    # Status field: "new", "reviewing", "mastered" (default "new")
    status = models.CharField(max_length=20, default="new")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.owner.username} - {self.topic or 'General'}"

