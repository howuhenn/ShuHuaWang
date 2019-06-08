# coding=utf-8

# @Time    : 2019/06/05 22:24
# @Author  : fertast
# @File    : models.py
# @Software: PyCharm

from django.db import models
from django.contrib.auth.models import AbstractUser
from db.base_model import BaseModel


class User(AbstractUser, BaseModel):
    """用户模型类"""

    class Meta:
        db_table = 'shw_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class Address(BaseModel):
    """地址模型类"""

    user = models.ForeignKey('User', verbose_name='所属用户')
    area_code = models.ForeignKey('Area', verbose_name='区域code')
    street = models.CharField(max_length=30, verbose_name='街道/镇')
    addr = models.CharField(max_length=256, verbose_name='详细地址')
    zip_code = models.CharField(max_length=6, verbose_name='邮政编码')
    receiver = models.CharField(max_length=20, verbose_name='收货人姓名')
    phone = models.CharField(max_length=11, verbose_name='手机号码')
    is_default = models.BooleanField(default=False, verbose_name='是否默认')

    class Meta:
        db_table = 'shw_address'
        verbose_name = '地址'
        verbose_name_plural = verbose_name


class Area(models.Model):
    """区域code"""

    area_code = models.CharField(max_length=6, verbose_name='区域code', primary_key=True)
    area_name = models.CharField(max_length=20, verbose_name='区域名称')
    in_code = models.CharField(max_length=6, verbose_name='所属区域code')

    class Meta:
        db_table = 'shw_area'
        verbose_name = '区域'
        verbose_name_plural = verbose_name



