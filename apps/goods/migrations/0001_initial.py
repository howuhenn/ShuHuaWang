# Generated by Django 2.2.1 on 2019-06-30 14:34

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('goods_name', models.CharField(max_length=20, verbose_name='商品名称')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='商品价格')),
                ('unit', models.CharField(max_length=20, verbose_name='单位')),
                ('stock', models.IntegerField(default=1, verbose_name='库存')),
                ('sales', models.IntegerField(default=0, verbose_name='销量')),
                ('desc', models.CharField(max_length=256, verbose_name='商品简介')),
                ('detail', tinymce.models.HTMLField(blank=True, verbose_name='详细介绍')),
                ('shelf_time', models.DateTimeField(auto_now=True, verbose_name='上架时间')),
                ('status', models.SmallIntegerField(choices=[(0, '下线'), (1, '上线')], default=1, verbose_name='商品状态')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
                'db_table': 'shw_goods',
            },
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('typ_name_1', models.CharField(max_length=10, verbose_name='商品种类1')),
                ('typ_name_2', models.CharField(max_length=10, verbose_name='商品种类2')),
            ],
            options={
                'verbose_name': '商品种类表',
                'verbose_name_plural': '商品种类表',
                'db_table': 'shw_goods_type',
            },
        ),
        migrations.CreateModel(
            name='GoodsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('image', models.ImageField(upload_to='goods', verbose_name='图片路径')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='商品')),
            ],
            options={
                'verbose_name': '商品图片',
                'verbose_name_plural': '商品图片',
                'db_table': 'df_goods_image',
            },
        ),
        migrations.CreateModel(
            name='GoodsEva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('access', models.CharField(max_length=256, verbose_name='评价内容')),
                ('access_level', models.SmallIntegerField(choices=[(1, '好评'), (2, '中评'), (3, '差评')], default=1, verbose_name='商品评价')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='商品')),
            ],
            options={
                'verbose_name': '商品评价',
                'verbose_name_plural': '商品评价',
                'db_table': 'shw_goods_eva',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsType', verbose_name='商品种类'),
        ),
    ]
