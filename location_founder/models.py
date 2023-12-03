from django.db import models

# Create your models here.
class Info(models.Model):
    key=models.CharField(max_length=200,blank=True)
    
