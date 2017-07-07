from django.db import models
from django.utils import timezone

class Post(models.Model):
    vocabulary = models.CharField(max_length=20)
    meaning = models.CharField(max_length=20)
    reference = models.CharField(max_length=500)
    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.vocabulary
