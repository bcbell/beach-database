from django.db import models

# Create your models here.
class Beach (models.Model):
    name= models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.name