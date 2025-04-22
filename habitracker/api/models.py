from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Habit(models.Model):
    FREQUENCY_CHOICES = [
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
    ]
    
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    name        = models.CharField(max_length=100)
    frequency   = models.CharField(max_length=50, choices=FREQUENCY_CHOICES)
    created_at  = models.DateTimeField(auto_now_add=True)