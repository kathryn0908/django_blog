from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=50)
    url = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


