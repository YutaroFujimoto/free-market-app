from django.db import models

# Create your models here.
# 商品のテーブル
class Product(models.Model):
    name = models.CharField(null=True, max_length=200)
    genre = models.CharField(null=True, max_length=200)
    explanation = models.TextField()
    condition = models.CharField(blank=False, null=True, max_length=200)
    price = models.IntegerField(null=True)
    shipping_cost = models.CharField(null=True, max_length=200)
    picture_1 = models.ImageField(upload_to='images/')
    picture_2 = models.ImageField(upload_to='images/')
    picture_3 = models.ImageField(upload_to='images/')
    picture_4 = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.name


#ユーザーデータのテーブル
class Userdata(models.Model):
    title = models.CharField(null=True, max_length=200)
    password = models.CharField(null=True, max_length=200)
    name = models.CharField(null=True, max_length=200)
    address = models.CharField(null=True, max_length=200)
    mail = models.CharField(null=True, max_length=200)
    line = models.CharField(blank=True, null=True, max_length=200)
    twitter = models.CharField(blank=True, null=True, max_length=200)
    text = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return self.name

#ログインしているユーザー
class Loginuser(models.Model):
    title = models.CharField(null=True, max_length=200)
    password = models.CharField(null=True, max_length=200)
    name = models.CharField(null=True, max_length=200)
    address = models.CharField(null=True, max_length=200)
    mail = models.CharField(null=True, max_length=200)
    line = models.CharField(blank=True, null=True, max_length=200)
    twitter = models.CharField(blank=True, null=True, max_length=200)
    text = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return self.name




