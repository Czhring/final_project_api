from django.db import models
from django.contrib.auth import get_user_model

class Idea(models.Model):
  title = models.CharField(max_length=100)
  content = models.CharField(max_length=1000)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return {self.title},{self.content},{self.owner}