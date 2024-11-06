from django.db import models
from django.utils import timezone

class BlogPost(models.Model):
    title = models.CharField(max_length=180)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Create your models here.
