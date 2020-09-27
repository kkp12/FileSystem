# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime

# Create your models here.

class Upload(models.Model):
    DownloadDocount = models.IntegerField(verbose_name=u"访问次数",default=0)
    #key to specify file
    code = models.CharField(max_length=8,verbose_name=u"code")
    #这里datetime.now不能加括号，否则变成模型创建时间
    Datatime = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")
    path = models.CharField(max_length=32,verbose_name=u"下载路径")
    name = models.CharField(max_length=32,verbose_name=u"文件名",default="")
    Filesize = models.CharField(max_length=10,verbose_name=u"文件大小")
    PCIP = models.CharField(max_length=32,verbose_name=u"IP地址",default="")

    class Meta():
        """ Meta 可用于定义数据表名，排序方式等。"""
        # 指明一个易于理解和表示的单词形式的对象。
        verbose_name="download"
        # 声明数据表的名。
        db_table = "download"
    
    def __str__(self):
        """表示查询时，返回name字段"""
        return self.name
