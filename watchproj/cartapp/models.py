from django.db import models
from cartapp.models import models
from watchapp.models import Product
# Create your models here.
class Cart(models.Model):
    user=models.CharField(max_length=200)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    class Meta:
        db_table='cart'


# def __str__(self):
#     return self.product
