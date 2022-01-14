from django.db import models
from location.models import locations
from product.models import products

# Create your models here.
class balance(models.Model):
    bid=models.IntegerField(primary_key=True)
    pid=models.ForeignKey(products,on_delete=models.CASCADE,blank=True)
    warehouse=models.ForeignKey(locations,on_delete=models.CASCADE,blank=True)
    qty=models.IntegerField()
    class Meta:
        ordering = ['bid']