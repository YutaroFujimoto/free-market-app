from django.db import models

# Create your models here.

from django.utils import timezone

class Article(models.Model):
    name=models.CharField(max_length=50)
    genre=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    price=models.IntegerField(default=0)
    picture=わからない
    carry=models.IntegerField(default=0)


    def __str__(self):
        return self.title