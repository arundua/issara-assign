# issaraAssign/models.py
from django.db import models

class CarDealer(models.Model):
    name = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255, null=True, blank=True)
    license_number = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    logo = models.URLField(max_length=500, null=True, blank=True)
    email = models.EmailField()
    rating_score = models.FloatField()
    rating_count = models.IntegerField()
    comments_count = models.IntegerField()
    popularity = models.IntegerField()
    # city = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name
