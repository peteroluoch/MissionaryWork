from django.db import models
from django.utils import timezone

class MissionaryPhoto(models.Model):
    """Model for storing missionary photos"""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=100)
    date_taken = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to='missionary_photos/')
    category = models.CharField(
        max_length=100,
        choices=[
            ('South Sudan', 'South Sudan'),
            ('Kenya', 'Kenya'),
            ('Rwanda', 'Rwanda'),
            ('Global Missionary Work', 'Global Missionary Work'),
            ('Glimpses of Our Mission Work', 'Glimpses of Our Mission Work'),
            ('Support Our Global Mission', 'Support Our Global Mission'),
        ],
        default='South Sudan'
    )
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    CARD_CHOICES = [
    (1, 'Card 1 - Gospel Outreach'),
    (2, 'Card 2 - Church Building'),
    (3, 'Card 3 - Community Support'),
]

    card_position = models.PositiveSmallIntegerField(
    choices=CARD_CHOICES,
    blank=True,
    null=True,
    help_text="Assign a specific card position (1-3) for homepage display."
)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Missionary Photo"
        verbose_name_plural = "Missionary Photos"
        ordering = ['-date_taken']
