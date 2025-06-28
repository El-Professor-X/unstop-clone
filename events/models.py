from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  date = models.DateTimeField()
  organizer = models.ForeignKey(User, on_delete=models.CASCADE)

class EventRegistration(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  event = models.ForeignKey(Event, on_delete=models.CASCADE)
  registered_on = models.DateTimeField(auto_now_add=True)
