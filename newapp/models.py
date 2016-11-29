# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from redactor.fields import RedactorField

from simple_app.models import image_upload_to


class Region(models.Model):
    class Meta:
        verbose_name = 'НКО'
        verbose_name_plural = 'НКО'
        ordering = ['name']

    name = models.CharField(max_length=1000, verbose_name='Область')

    def __unicode__(self):
        return self.name


class NKO(models.Model):
    class Meta:
        verbose_name = 'НКО'
        verbose_name_plural = 'НКО'

    region = models.ForeignKey(Region, null=True, blank=True)
    title_ru = models.CharField(max_length=1000, verbose_name='Название')
    text_ru = RedactorField(verbose_name='Текст',
                            upload_to=image_upload_to,
                            redactor_options={'buttons': ['image'],},
                            allow_image_upload=True,
                            allow_file_upload=True)
    manager = models.CharField(max_length=1000, verbose_name='Менеджер')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    address = models.TextField(verbose_name='Адрес')
    phone_number = models.CharField(max_length=100, verbose_name='Номер телефона')
    phone_number_1 = models.CharField(max_length=100, verbose_name='Экстра номер 1', null=True, blank=True)
    mail = models.CharField(max_length=100, verbose_name='e-Mail', null=True, blank=True)

    def __unicode__(self):
        return self.title_ru


class NKOKG(models.Model):
    class Meta:
        verbose_name = 'НКО кыргызча'
        verbose_name_plural = 'НКО кыргызча'

    region = models.ForeignKey(Region, null=True, blank=True)
    title_ru = models.CharField(max_length=1000, verbose_name='Название')
    text_ru = RedactorField(verbose_name='Текст',
                            upload_to=image_upload_to,
                            allow_image_upload=True,
                            allow_file_upload=True)
    manager = models.CharField(max_length=1000, verbose_name='Менеджер')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    address = models.TextField(verbose_name='Адрес')
    phone_number = models.CharField(max_length=100, verbose_name='Номер телефона')
    phone_number_1 = models.CharField(max_length=100, verbose_name='Экстра номер 1', null=True, blank=True)
    mail = models.CharField(max_length=100, verbose_name='e-Mail', null=True, blank=True)

    def __unicode__(self):
        return self.title_ru
