# coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Embassy(models.Model):
    class Meta:
        verbose_name = 'посольство'
        verbose_name_plural = 'Посольства'
        ordering = 'country'.split()

    country = models.CharField(max_length=100, verbose_name='Страна')
    phone_number = models.CharField(max_length=100, verbose_name='Номер телефона')
    fax = models.CharField(max_length=100, verbose_name='Факс')
    email = models.EmailField(max_length=100, verbose_name='Электронная почта')
    site = models.CharField(null=True, blank=True, default='сайта нет', verbose_name='Сайт', max_length=100)
    address = models.TextField(verbose_name='Адрес')

    def __unicode__(self):
        return self.country


class Consulate(models.Model):
    class Meta:
        verbose_name_plural = 'Общественные представители'
        verbose_name = 'общественный представитель'
        ordering = 'region'.split()
    embassy = models.ForeignKey(Embassy)
    region = models.CharField(max_length=1000, verbose_name='Регион')
    address = models.TextField(verbose_name='Адрес')
    phone_number = models.CharField(max_length=100, verbose_name='Номер телефона')

    def __unicode__(self):
        return self.region
