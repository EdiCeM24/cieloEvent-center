from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField(max_length=300)
    price = models.FloatField()
    image_url = models.CharField(max_length=2083)

