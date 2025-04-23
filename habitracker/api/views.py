from django.shortcuts import render
from rest_framework import viewsets
from .models import Habit
from .serializers import HabitSerializer

from django.contrib.auth import get_user_model
from django.http import HttpResponse

def create_superuser(request):
    User = get_user_model()
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "admin")
        return HttpResponse("Superuser created!")
    return HttpResponse("Superuser already exists.")

# Create your views here.
class HabitViewSet(viewsets.ModelViewSet):
    queryset    =   Habit.objects.all()
    serializer_class    =   HabitSerializer