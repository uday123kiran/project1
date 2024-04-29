from django.db import models

# Create your models here.
class lenovo(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    foodtype=models.CharField(max_length=50)
    image=models.ImageField( upload_to="")
    video=models.FileField( upload_to="")

