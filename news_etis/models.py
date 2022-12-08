from django.db import models
from PIL import Image

# Create your models here.

class Profile(models.Model):
    login = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    

    def __str__(self):
        return self.login


class News(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=255)
    discription = models.CharField(max_length=255)


    def __str__(self):
        return self.name