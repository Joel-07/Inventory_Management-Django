from django.db import models

# Create your models here.
class products(models.Model):
    pid=models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=50)
    qty=models.CharField(max_length=50)
    def __str__(self):
        return self.pname
    class Meta:
        ordering = ['pid']
