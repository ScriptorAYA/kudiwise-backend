from django.db import models
from users.models import User

class Lesson(models.Model):
    DIALECT_CHOICES = [
        ('hausa', 'Hausa'),
        ('asante', 'Asante Twi')
    ]
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')
    ]
    title = models.CharField(max_length=200)
    content = models.TextField()
    dialect = models.CharField(max_length=10, choices=DIALECT_CHOICES)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.dialect})"

class UserLessonProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lesson_progress')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='user_progress')
    completion_status = models.CharField(max_length=20, default='incomplete')
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.lesson.title} - {self.completion_status}"

