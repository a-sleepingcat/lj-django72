from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=80)
    password = models.CharField(max_length=256)
    tel = models.CharField(max_length=30)

    #获取唯一标识符，令牌
    token = models.CharField(max_length=256,default='')

#轮播图
class Wheel(models.Model):
    #图片名称
    img = models.CharField(max_length=100, )


# 商品详情
class Goods(models.Model):
    name = models.CharField(max_length=256)
    price = models.CharField(max_length=30)
    detail = models.CharField(max_length=256,default='')
    unit = models.CharField(max_length=10)
    headImg = models.CharField(max_length=120)
    img1 = models.CharField(max_length=120)
    img2 = models.CharField(max_length=120)
    img3 = models.CharField(max_length=120)
    img4 = models.CharField(max_length=120)
    img5 = models.CharField(max_length=120)
    img6 = models.CharField(max_length=120)
    img7 = models.CharField(max_length=120)
    img13 = models.CharField(max_length=120)
    img19 = models.CharField(max_length=120)
    img20= models.CharField(max_length=120)
    total = models.CharField(max_length=100)
    potol = models.CharField(max_length=100)


