from django.db import models

# Create your models here.
class ProductDetails(models.Model):
    brand = models.CharField(max_length=30)
    name = models.CharField(max_length=500)
    price = models.FloatField()

    def __str__(self):
       return self.name