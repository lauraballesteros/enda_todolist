from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class todoItem(models.Model):
    content = models.TextField()
    is_completed = models.BooleanField(default=False)
