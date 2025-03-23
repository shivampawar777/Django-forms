from django.db import models

# Create your models here.
class Formdata(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    rating=models.IntegerField()
    feedback=models.CharField(max_length=2000)


