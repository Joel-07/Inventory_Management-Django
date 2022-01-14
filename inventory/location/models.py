from django.db import models

# Create your models here.
class locations(models.Model):
    lid=models.IntegerField(primary_key=True)
    location=models.CharField(max_length=50)
    def __str__(self):
        return self.location
    class Meta:
        ordering = ['lid']