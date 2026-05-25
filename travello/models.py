from django.db import models

# Create your models here.

class destination(models.Model):
    
    name=models.CharField(max_length=100)
    description=models.TextField(default="sample")
    image=models.ImageField( upload_to='pics')
    price=models.IntegerField(default=0)
    offer=models.BooleanField(default=False)

