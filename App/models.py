from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=80)
    password = models.CharField(max_length=256)
    tel = models.CharField(max_length=30)

    #获取唯一标识符，令牌
    token = models.CharField(max_length=256,default='')