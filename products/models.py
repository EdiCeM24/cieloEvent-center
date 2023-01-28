from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField(max_length=300)
    price = models.FloatField()
    image_url = models.CharField(max_length=2083)


class Home(models.Model):
    username = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=8)
    confirm_password = models.CharField(max_length=8)   


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=15)
    discount = models.FloatField()