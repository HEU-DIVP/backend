from django.db import models
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=16, verbose_name='文章来源')


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='文章标题')
    source = models.ForeignKey(Category, on_delete=models.PROTECT)
    url = models.URLField(verbose_name='文章链接')
    click_count = models.IntegerField(verbose_name='点击量')
    create_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间')
