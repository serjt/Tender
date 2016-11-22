# coding=utf-8
from __future__ import unicode_literals

from django.db import models


def image_upload_to(instance, filename):
    return "images/%s" % filename


# Create your models here.

class Embassy(models.Model):
    class Meta:
        verbose_name = 'посольство'
        verbose_name_plural = 'Посольства'
        ordering = 'country'.split()

    image = models.ImageField(upload_to=image_upload_to, verbose_name='Иконка', null=True)
    country = models.CharField(max_length=100, verbose_name='Страна')
    phone_number = models.CharField(max_length=100, verbose_name='Номер телефона')
    phone_number_1 = models.CharField(max_length=100, verbose_name='Экстра номер 1', null=True, blank=True)
    phone_number_2 = models.CharField(max_length=100, verbose_name='Экстра номер 2', null=True, blank=True)
    fax = models.CharField(max_length=100, verbose_name='Факс')
    fax_1 = models.CharField(max_length=100, verbose_name='Факс 1', null=True, blank=True)
    fax_2 = models.CharField(max_length=100, verbose_name='Факс 2', null=True, blank=True)
    email = models.EmailField(max_length=100, verbose_name='Электронная почта')
    site = models.CharField(null=True, blank=True, verbose_name='Сайт', max_length=100)
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
    phone_number_1 = models.CharField(max_length=100, verbose_name='Экстра номер 1', null=True, blank=True)
    phone_number_2 = models.CharField(max_length=100, verbose_name='Экстра номер 2', null=True, blank=True)

    def __unicode__(self):
        return self.region


class CountriesAll(models.Model):
    class Meta:
        verbose_name = 'диаспору'
        verbose_name_plural = 'Диаспоры'

    country = models.CharField(max_length=100, verbose_name='Страна')
    image = models.ImageField(upload_to=image_upload_to, verbose_name='Иконка')

    def __unicode__(self):
        return self.country


class Diaspora(models.Model):
    class Meta:
        verbose_name = 'диаспору'
        verbose_name_plural = 'Диаспоры'

    country = models.ForeignKey(CountriesAll, null=True, verbose_name='Страна')
    manager = models.CharField(max_length=1000, verbose_name='Ф.И.О.')
    place = models.TextField(verbose_name='Место работы')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    address = models.TextField(verbose_name='Адрес', null=True, blank=True)
    phone_number = models.CharField(max_length=100, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='E-mail', null=True, blank=True)
    city = models.CharField(verbose_name='Город', max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.country.country
