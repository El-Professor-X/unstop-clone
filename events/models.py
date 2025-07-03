from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ('hiring', 'Hiring Challenge'),
    ('quiz', 'Quiz/Trivia'),
    ('hackathon', 'Hackathon'),
    ('internship', 'Internship'),
    ('other', 'Other'),
]

class Event(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  date = models.DateTimeField()
  organizer = models.ForeignKey(User, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='event_images/', default='event_images/default.jpg')
  category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')  # ✅ NEW


class EventRegistration(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  event = models.ForeignKey(Event, on_delete=models.CASCADE)
  registered_on = models.DateTimeField(auto_now_add=True)
