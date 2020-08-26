from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class todoItem(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    is_completed = models.BooleanField(default=False)
