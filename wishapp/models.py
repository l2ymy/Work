# _*_ coding: utf-8 _*_

from django.db import models

MAX_LENGTH = 255

class Machine(models.Model):
    u"""検証機器のデータテーブル"""
    author = models.CharField('担当者', max_length=MAX_LENGTH)
    vender = models.CharField('メーカー', max_length=MAX_LENGTH)
    name = models.CharField('名称', max_length=MAX_LENGTH)
    cpuinfo = models.CharField('CPU', max_length=MAX_LENGTH, blank=True)
    meminfo = models.CharField('Memory', max_length=MAX_LENGTH, blank=True)
    nicinfo = models.CharField('NIC情報', max_length=MAX_LENGTH, blank=True)
    biosinfo = models.CharField('BIOSバージョン', max_length=MAX_LENGTH, blank=True)

    def __str__(self):
        return self.name


class Borrowed(models.Model):
    u"""借用物管理のデータテーブル"""
    CHECK_CHOICES = (
            ('○', 'OK'),('-', 'NG')
            )

    borrow_personnel = models.CharField('借用担当者', max_length=MAX_LENGTH, blank=True)
    borrow_name = models.CharField('名称', max_length=MAX_LENGTH, blank=True)
    borrow_date = models.DateTimeField('借用日')
    borrow_check = models.CharField('借用時チェック', max_length=2, choices=CHECK_CHOICES)
    return_date = models.DateTimeField('返却日')

    def __str__(self):
        return self.name


