# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 11:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='分类名称')),
                ('sort', models.IntegerField(default=0, verbose_name='排序值')),
                ('is_root', models.BooleanField(default=False, verbose_name='是否是一级分类')),
                ('image', models.ImageField(blank=True, null=True, upload_to='category/%Y/%m', verbose_name='分类图片')),
                ('is_abort', models.BooleanField(default=False, verbose_name='是否删除')),
                ('parent', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='product.Category', verbose_name='上级分类')),
            ],
            options={
                'verbose_name_plural': '分类',
                'verbose_name': '分类',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='产品名称')),
                ('unit', models.CharField(max_length=100, verbose_name='单位')),
                ('keywords', models.CharField(max_length=200, verbose_name='关键词')),
                ('image', models.ImageField(upload_to='product/%Y/%m', verbose_name='产品图片')),
                ('barcode', models.CharField(max_length=100, verbose_name='条码')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='售价')),
                ('market_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='市场价')),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='成本价')),
                ('count', models.IntegerField(default=0, verbose_name='库存')),
                ('sales_count', models.IntegerField(default=0, verbose_name='售出数量')),
                ('is_show_sales_count', models.BooleanField(default=False, verbose_name='显示销量')),
                ('has_invoice', models.BooleanField(default=False, verbose_name='提供发票')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('status', models.IntegerField(choices=[(0, '下架'), (1, '上架')], verbose_name='状态')),
                ('no_search', models.BooleanField(default=False, verbose_name='搜索是否显示')),
                ('cannot_refund', models.BooleanField(default=False, verbose_name='支持退换货')),
                ('order_value', models.IntegerField(default=0, verbose_name='排序值')),
                ('view_count', models.IntegerField(default=0, verbose_name='浏览量')),
                ('details', models.TextField(verbose_name='详情')),
                ('is_abort', models.BooleanField(default=False, verbose_name='是否删除')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Category', verbose_name='分类')),
            ],
            options={
                'verbose_name_plural': '产品',
                'verbose_name': '产品',
            },
        ),
    ]
