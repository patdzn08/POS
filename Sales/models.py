from django.db import models
from django.db.models.fields import AutoField
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Product (models.Model):
    product_id =models.BigAutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_des=models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=2,max_digits=10)
    date_posted= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('Sales-home')

class CustomerOrder (models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    items = models.ManyToManyField('Product', related_name='item', blank=True)

    def get_absolute_url(self):
        return reverse('Sales-home')

class GenerateTransaction (models.Model):
    product_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=2,max_digits=10)
    items = models.ManyToManyField('Product', related_name='order', blank=True)

    def get_absolute_url(self):
        return reverse('Sales-POS')


    
    
    

    

