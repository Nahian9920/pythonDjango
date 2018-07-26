from django.db import models

# Create your models here.
class DailyCost(models.Model):
    expence=models.CharField(max_length=100)
    purpose=models.CharField(max_length=30)
    def __str__(self):
        return self.purpose
       # return self.expence





class Demo(models.Model):
    aa = models.CharField(max_length=100)
    bb = models.CharField(max_length=30)

