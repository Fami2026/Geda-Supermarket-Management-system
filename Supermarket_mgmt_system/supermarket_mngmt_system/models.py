from django.db import models

# Create your models here.
class  Product (models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.TextField(max_length=100, unique=True)
    quantity=models.PositiveIntegerField(blank=True,null=True)
    unit_price =models.FloatField(null=True,blank=True)
    stock_level =models.PositiveSmallIntegerField(blank=True,null=True)
    created_by_id=models.PositiveIntegerField(default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name + " ="+str(self.quantity)
