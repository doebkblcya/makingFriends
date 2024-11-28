from django.contrib.auth.models import AbstractUser  # 导入 Django 提供的 AbstractUser 基类
from django.db import models  # 导入 Django 的模型模块

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # 自定义字段
    birthday = models.DateField(null=True, blank=True)  # 生日
    phone_number = models.CharField(max_length=15, blank=True)  # 电话号码
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)  # 头像

    # 大区字段
    REGION_CHOICES = [
        ('A1', '联盟一区'),
        ('A2', '联盟二区'),
        ('A3', '联盟三区'),
        ('A4', '联盟四区'),
        ('A5', '联盟五区'),
        ('IONIA', '艾欧尼亚'),
        ('ROSE', '黑色玫瑰'),
        ('SUMMITS', '峡谷之巅'),
    ]
    region = models.CharField(max_length=10, choices=REGION_CHOICES, blank=True)  # 大区字段

    # 段位字段（从低到高）
    TIER_CHOICES = [
        ('IRON', '坚韧黑铁'),
        ('BRONZE', '英勇黄铜'),
        ('SILVER', '不屈白银'),
        ('GOLD', '荣耀黄金'),
        ('PLATINUM', '华贵铂金'),
        ('EMERALD', '流光翡翠'),
        ('DIAMOND', '璀璨钻石'),
        ('MASTER', '超凡大师'),
        ('GRANDMASTER', '傲世宗师'),
        ('CHALLENGER', '最强王者'),
    ]
    tier = models.CharField(max_length=12, choices=TIER_CHOICES, blank=True)  # 段位字段

    def __str__(self):
        return self.username

