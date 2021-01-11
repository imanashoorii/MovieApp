from django.db import models


# Create your models here.

class MovieData(models.Model):
    CATEGORY = (
        ('AC', 'Action'),
        ('DR', 'Dram'),
        ('CO', 'Comedy'),

    )
    name = models.CharField(max_length=100)
    duration = models.FloatField()
    rating = models.FloatField()
    category = models.CharField(choices=CATEGORY, max_length=10, default='Action')
    image = models.ImageField(upload_to='Images/', default='Images/No_image_available.png')

    def __str__(self):
        return self.name
