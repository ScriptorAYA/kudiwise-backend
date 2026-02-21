from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    DIALECT_CHOICES = [
        ('hausa', 'Hausa'),
        ('asante', 'Asante Twi')
    ]
    dialect_preference = models.CharField(
        max_length=10,
        choices=DIALECT_CHOICES,
        default='hausa'
    )

    def __str__(self):
        return self.username

