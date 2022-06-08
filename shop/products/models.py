from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120) 
    description = models.TextField(blank=True, null=True)
    summary = models.TextField(default='Hello this is awesome!')

    def __str__(self):
        return self.title
    