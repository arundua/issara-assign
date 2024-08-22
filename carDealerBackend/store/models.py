from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from datetime import timedelta

class KeyValue(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.TextField()  # To handle arbitrary length values
    created_at = models.DateTimeField(auto_now_add=True)
    ttl = models.DurationField(default=timedelta(minutes=5))  # Default TTL is 5 minutes

    def is_expired(self):
        return timezone.now() > self.created_at + self.ttl

    def reset_ttl(self):
        self.created_at = timezone.now()
        self.save()
