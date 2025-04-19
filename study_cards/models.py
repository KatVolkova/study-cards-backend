from django.db import models
from django.contrib.auth.models import User


class Flashcard(models.Model):
    # The owner of the flashcard
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="flashcards"
        )
    question = models.TextField()
    answer = models.TextField()
    topic = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[('new', 'New'),
                 ('reviewing', 'Reviewing'),
                 ('mastered', 'Mastered')
                 ],
        default='new'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.owner.username} - {self.topic or 'General'}"


class ReviewHistory(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="review_sessions"
        )
    date = models.DateTimeField(auto_now_add=True)
    correct = models.IntegerField()
    total = models.IntegerField()
    score = models.DecimalField(max_digits=5, decimal_places=2)
    streak = models.IntegerField(default=0)
    
    def __str__(self):
        return (
            f"{self.user.username} -"
            f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} -"
            f"{self.score}%"
            )
