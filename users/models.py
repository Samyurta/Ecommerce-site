from django.db import models
from products.models import Product
from django.contrib.auth.models import User
from django.core.validators import *
from django.core import validators

# Create your models here.
class Cart(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_data=models.DateTimeField(auto_now_add=True)