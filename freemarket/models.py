from django.db import models

# Create your models here.
# 商品のテーブル
class Product(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    explanation = models.TextField()
    condition = models.CharField(max_length=200)
    price = models.IntegerField()
    shipping_cost = models.CharField(max_length=200)
    picture_1 = models.ImageField(upload_to='images/')
    picture_2 = models.ImageField(upload_to='images/')
    picture_3 = models.ImageField(upload_to='images/')
    picture_4 = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.name



class Userdata(models.Model):
    title = models.CharField(null = True, max_length=200)
    password = models.CharField(null = True, max_length=200)
    name = models.CharField(null = True, max_length=200)
    icon = models.CharField(null = True, max_length=200)
    address = models.CharField(null = True, max_length=200)
    mail = models.CharField(null = True, max_length=200)
    line = models.CharField(null = True, max_length=200)
    twitter = models.CharField(null = True, max_length=200)
    text = models.CharField(null = True, max_length=200)

