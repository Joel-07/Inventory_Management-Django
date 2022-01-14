from django.db import models
from location.models import locations
from product.models import products
# Create your models here.
class prod_move(models.Model):
    mid=models.IntegerField(primary_key=True)
    timestamp=models.CharField(max_length=100)
    f_location=models.CharField(max_length=50)
    t_location=models.CharField(max_length=50)
    pid=models.ForeignKey(products,on_delete=models.CASCADE)
    qty=models.IntegerField()
    class Meta:
        ordering = ['-mid']
