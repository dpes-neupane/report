from django.db import models
import os
import csv



# Create your models here.
class YearBarsa(models.Model):
    year_barsa = models.IntegerField(default=0)
    def __str__(self):
        return str(self.year_barsa)

class Product(models.Model):
    
    product = models.CharField(max_length=50)
    def __str__(self):
        return self.product

class Sales(models.Model):
    year_sales = models.ForeignKey(YearBarsa, on_delete=models.CASCADE)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    sales = models.IntegerField(default=0)  
    def __str__(self):
        return str(self.sales)




    