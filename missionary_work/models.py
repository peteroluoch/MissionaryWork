from django.db import models
from django.utils import timezone

class MissionaryPhoto(models.Model):
    """Model for storing missionary photos"""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=100)
    date_taken = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to='missionary_photos/')
    category = models.CharField(max_length=100, default='South Sudan')
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Missionary Photo"
        verbose_name_plural = "Missionary Photos"
        ordering = ['-date_taken']
