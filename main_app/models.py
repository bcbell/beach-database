from django.db import models
from django.urls import reverse

# Create your models here.

TYPE=(
    ('O', 'Ocean'),
    ('L', 'Lake'),
    ('R', 'River')
)
class Beach (models.Model):
    name= models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"beach_id": self.id})

class Water(models.Model):
    visit= models.DateField('visit date')
    type = models.CharField(
        max_length=1,
        choices=TYPE,
        default=TYPE[0][0]
        )
    
    beach = models.ForeignKey(Beach, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_type_display()} on {self.visit}"
    
    class Meta:
        ordering=['-visit']