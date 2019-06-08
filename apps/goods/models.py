# coding=utf-8

# @Time    : 2019/06/08 13:06
# @Author  : fertast
# @File    : models.py
# @Software: PyCharm

from db.base_model import BaseModel
from django.db import models
from tinymce.models import HTMLField


class GoodsType(BaseModel):
    """商品种类模型类"""

    typ_name_1 = models.CharField(max_length=10, verbose_name='商品种类1')
    typ_name_2 = models.CharField(max_length=10, verbose_name='商品种类2')

    class Meta:

        db_table = 'shw_goods_type'
        verbose_name = '商品种类表'
        verbose_name_plural = verbose_name


class Goods(BaseModel):
    """商品模型类"""

    status_choices = (
        (0, '下线'),
        (1, '上线'),
    )

    user = models.ForeignKey('user.User', verbose_name='用户')
    type = models.ForeignKey('GoodsType', verbose_name='商品种类')
    goods_name = models.CharField(max_length=20, verbose_name='商品名称')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品价格')
    unit = models.CharField(max_length=20, verbose_name='单位')
    stock = models.IntegerField(default=1, verbose_name='库存')
    sales = models.IntegerField(default=0, verbose_name='销量')
    # 富文本类型:带有格式的文本
    detail = HTMLField(blank=True, verbose_name='详细介绍')
    shelf_time = models.DateTimeField(auto_now=True, verbose_name='上架时间')
    status = models.SmallIntegerField(default=1, choices=status_choices, verbose_name='商品状态')

    class Meta:
        db_table = 'shw_goods'
        verbose_name = '商品'
        verbose_name_plural = verbose_name


class GoodsEva(BaseModel):
    """商品评价"""

    access_level_choices = (
        (1, '好评'),
        (2, '中评'),
        (3, '差评'),
    )

    goods = models.ForeignKey('Goods', verbose_name='商品')
    access = models.CharField(max_length=256, verbose_name='评价内容')
    access_level = models.SmallIntegerField(default=1, choices=access_level_choices, verbose_name='商品评价')

    class Meta:
        db_table = 'shw_goods_eva'
        verbose_name = '商品评价'
        verbose_name_plural = verbose_name


class GoodsImage(BaseModel):
    """商品图片模型类"""

    goods = models.ForeignKey('Goods', verbose_name='商品')
    image = models.ImageField(upload_to='goods', verbose_name='图片路径')

    class Meta:
        db_table = 'df_goods_image'
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name
