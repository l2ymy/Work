# _*_ coding: utf-8 _*_

from django.db import models

class Machine(models.Model):
    """機器"""
    author = models.CharField('担当者', max_length=255)
    vender = models.CharField('メーカー', max_length=255)
    name = models.CharField('名称', max_length=255)
    cpuinfo = models.CharField('CPU', max_length=255, blank=True)
    meminfo = models.CharField('Memory', max_length=255)
    nicinfo = models.CharField('NIC情報', max_length=255)
    biosinfo = models.CharField('BIOSバージョン', max_length=255)

    def __str__(self):
        return self.name



