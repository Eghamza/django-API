from django.db import models

# Create your models here.
class drinks(models.Model):
    name = models.CharField(max_length=222)
    description = models.CharField(max_length=222)
    
    def __str__(self):
        return self.name +" "+ self.description
    