# coding=utf-8
from __future__ import unicode_literals
from redactor.fields import RedactorField
from django.utils.text import slugify
from django.db import models


# Create your models here.

def image_upload_to(instance, filename):
    return "images/%s" % filename


class News(models.Model):
    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'Новости'

    image = models.ImageField(upload_to=image_upload_to, verbose_name='Картинка', null=True, blank=True)
    title_ru = models.CharField(max_length=1000, verbose_name='Заголовок')
    text_ru = RedactorField(verbose_name='Текст',
                            upload_to=image_upload_to,
                            allow_image_upload=True,
                            allow_file_upload=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __unicode__(self):
        return self.title_ru

    @staticmethod
    def autocomplete_search_fields():
        return 'title_ru'


class NewsKg(models.Model):
    class Meta:
        verbose_name = 'жаңылык'
        verbose_name_plural = 'жаңылыктар'

    image = models.ImageField(upload_to=image_upload_to, verbose_name='Картинка', null=True, blank=True)
    title_ru = models.CharField(max_length=1000, verbose_name='Заголовок')
    text_ru = RedactorField(verbose_name='Текст',
                            upload_to=image_upload_to,
                            allow_image_upload=True,
                            allow_file_upload=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __unicode__(self):
        return self.title_ru

    @staticmethod
    def autocomplete_search_fields():
        return 'title_ru'


class Country(models.Model):
    class Meta:
        verbose_name = 'правило пребывания в ЕАЭС'
        verbose_name_plural = 'Правила пребывания в ЕАЭС'
        ordering = ['country']

    country = models.CharField(max_length=100, verbose_name='Страна')
    image = models.ImageField(upload_to=image_upload_to, verbose_name='Иконка')

    def __unicode__(self):
        return self.country


class RulesOfIncomingEAES(models.Model):
    class Meta:
        verbose_name = 'правило пребывания в ЕАЭС'
        verbose_name_plural = 'Правила пребывания в ЕАЭС'

    country = models.ForeignKey(Country, null=True, blank=True)
    title_ru = models.CharField(max_length=1000, verbose_name='Заголовок')
    text_ru = RedactorField(verbose_name='Текст',
                            upload_to=image_upload_to,
                            allow_image_upload=True,
                            allow_file_upload=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __unicode__(self):
        return self.title_ru

    @staticmethod
    def autocomplete_search_fields():
        return 'title_ru'


class RulesOfIncomingKgEAES(models.Model):
    class Meta:
        verbose_name = 'ЕАЭСте жүрүү эреже'
        verbose_name_plural = 'ЕАЭСте жүрүү эреже'

    country = models.ForeignKey(Country, null=True, blank=True)
    title_ru = models.CharField(max_length=1000, verbose_name='Заголовок')
    text_ru = RedactorField(verbose_name='Текст',
                            upload_to=image_upload_to,
                            allow_image_upload=True,
                            allow_file_upload=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __unicode__(self):
        return self.title_ru

    @staticmethod
    def autocomplete_search_fields():
        return 'title_ru'


class CountryAll(models.Model):
    class Meta:
        verbose_name = 'правило пребывания'
        verbose_name_plural = 'Правила пребывания'
        ordering = ['country']

    country = models.CharField(max_length=100, verbose_name='Страна')
    image = models.ImageField(upload_to=image_upload_to, verbose_name='Иконка')

    def __unicode__(self):
        return self.country


class RulesOfIncoming(models.Model):
    class Meta:
        verbose_name = 'правило пребывания'
        verbose_name_plural = 'Правила пребывания'

    country = models.ForeignKey(CountryAll, null=True, blank=True)
    title_ru = models.CharField(max_length=1000, verbose_name='Заголовок')
    text_ru = RedactorField(verbose_name='Текст',
                            upload_to=image_upload_to,
                            allow_image_upload=True,
                            allow_file_upload=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __unicode__(self):
        return self.title_ru

    @staticmethod
    def autocomplete_search_fields():
        return 'title_ru'


class RulesOfIncomingKg(models.Model):
    class Meta:
        verbose_name = 'чет өлкөдө жүрүү эреже'
        verbose_name_plural = 'Чет өлкөдө жүрүү эрежелер'

    country = models.ForeignKey(CountryAll, null=True, blank=True)
    title_ru = models.CharField(max_length=1000, verbose_name='Заголовок')
    text_ru = RedactorField(verbose_name='Текст',
                            upload_to=image_upload_to,
                            allow_image_upload=True,
                            allow_file_upload=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __unicode__(self):
        return self.title_ru

    @staticmethod
    def autocomplete_search_fields():
        return 'title_ru'


class Countries(models.Model):
    class Meta:
        verbose_name = 'Трудоустройство'
        verbose_name_plural = 'Трудоустройство'
        ordering = ['country']

    country = models.CharField(max_length=100, verbose_name='Страна')
    image = models.ImageField(upload_to=image_upload_to, verbose_name='Иконка')

    def __unicode__(self):
        return self.country


class Employment(models.Model):
    class Meta:
        verbose_name = 'Трудоустройство'
        verbose_name_plural = 'Трудоустройство'

    country = models.ForeignKey(Countries, null=True)
    name = models.CharField(max_length=1000, verbose_name='Заголовок')
    manager = models.CharField(max_length=1000, verbose_name='Менеджер')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    address = models.TextField(verbose_name='Адрес')
    phone_number = models.CharField(max_length=100, verbose_name='Номер телефона')
    phone_number_1 = models.CharField(max_length=100, verbose_name='Экстра номер 1', null=True, blank=True)
    phone_number_2 = models.CharField(max_length=100, verbose_name='Экстра номер 2', null=True, blank=True)
    map_link = models.TextField(verbose_name="Ссылка на карту", null=True, blank=True)

    def __unicode__(self):
        return self.name


class RulesOfMigration(models.Model):
    class Meta:
        verbose_name = 'торговля людьми'
        verbose_name_plural = 'торговля людьми'

    image = models.ImageField(upload_to=image_upload_to, verbose_name='Иконка')
    title_ru = models.CharField(max_length=1000, verbose_name='Заголовок')
    text_ru = RedactorField(verbose_name='Баяндоо',
                            upload_to=image_upload_to,
                            allow_image_upload=True,
                            allow_file_upload=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __unicode__(self):
        return self.title_ru


class RulesOfMigrationKg(models.Model):
    class Meta:
        verbose_name = 'адам аткезчилиги'
        verbose_name_plural = 'адам аткезчилиги'

    image = models.ImageField(upload_to=image_upload_to, verbose_name='Иконка')
    title_ru = models.CharField(max_length=1000, verbose_name='Заголовок')
    text_ru = RedactorField(verbose_name='Баяндоо',
                            upload_to=image_upload_to,
                            allow_image_upload=True,
                            allow_file_upload=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __unicode__(self):
        return self.title_ru


class RF(models.Model):
    class Meta:
        verbose_name = 'Запрет въезда в РФ'
        verbose_name_plural = 'Запрет въезда в РФ'

    image = models.ImageField(upload_to=image_upload_to, verbose_name='Иконка')
    title_ru = models.CharField(max_length=1000, verbose_name='Заголовок')
    text_ru = RedactorField(verbose_name='Баяндоо',
                            upload_to=image_upload_to,
                            allow_image_upload=True,
                            allow_file_upload=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __unicode__(self):
        return self.title_ru

    @staticmethod
    def autocomplete_search_fields():
        return 'title_ru'


class RFKG(models.Model):
    class Meta:
        verbose_name = 'орус федерациясына кирүүгө тыюу салуу'
        verbose_name_plural = 'Орус федерациясына кирүүгө тыюу салуу'

    image = models.ImageField(upload_to=image_upload_to, verbose_name='Иконка')
    title_ru = models.CharField(max_length=1000, verbose_name='Заголовок')
    text_ru = RedactorField(verbose_name='Баяндоо',
                            upload_to=image_upload_to,
                            allow_image_upload=True,
                            allow_file_upload=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __unicode__(self):
        return self.title_ru

    @staticmethod
    def autocomplete_search_fields():
        return 'title_ru'


class FAQ(models.Model):
    class Meta:
        verbose_name = 'вопрос и ответ'
        verbose_name_plural = 'Часто задаваемые вопросы'

    question_ru = RedactorField(verbose_name='Вопрос', upload_to=image_upload_to,
                                allow_image_upload=True,
                                allow_file_upload=True, null=True, blank=True)
    answer_ru = RedactorField(verbose_name='Ответ', upload_to=image_upload_to,
                              allow_image_upload=True,
                              allow_file_upload=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __unicode__(self):
        return self.question_ru


class FAQKG(models.Model):
    class Meta:
        verbose_name = 'суроо жооп'
        verbose_name_plural = 'Көп берилүүчү суроолор'

    question_ru = RedactorField(verbose_name='Суроо', upload_to=image_upload_to,
                                allow_image_upload=True,
                                allow_file_upload=True, null=True, blank=True)
    answer_ru = RedactorField(verbose_name='Жооп', upload_to=image_upload_to,
                              allow_image_upload=True,
                              allow_file_upload=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __unicode__(self):
        return self.question_ru


class CountryHotline(models.Model):
    class Meta:
        verbose_name = 'горячую линию'
        verbose_name_plural = 'Горячие линии'
        ordering = 'country'.split()

    country = models.CharField(max_length=100, verbose_name='Страна')
    image = models.ImageField(upload_to=image_upload_to, verbose_name='Иконка')

    def __unicode__(self):
        return self.country


class Hotline(models.Model):
    class Meta:
        verbose_name = 'горячую линию'
        verbose_name_plural = 'Горячие линии'

    country = models.ForeignKey(CountryHotline, verbose_name='Страна')
    title_ru = models.CharField(max_length=1000, verbose_name='Название горячей линии')
    phone_number = models.CharField(max_length=100, verbose_name='Номер телефона')

    def __unicode__(self):
        return self.title_ru


class HotlineKG(models.Model):
    class Meta:
        verbose_name = 'тынымсыз байланыш'
        verbose_name_plural = 'Тынымсыз байланыштар'

    country = models.ForeignKey(CountryHotline, verbose_name='Страна')
    title_ru = models.CharField(max_length=1000, verbose_name='Название горячей линии')
    phone_number = models.CharField(max_length=100, verbose_name='Номер телефона')

    def __unicode__(self):
        return self.title_ru
