from django.db import models

CATEGORY_CHOICES = [
    ('movie', 'Sinema Filmi'),
    ('series', 'Dizi'),
    ('documentary', 'Belgesel'),
]

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True) 
    release_date = models.DateField(null=True, blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    poster = models.CharField(null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='movie')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


