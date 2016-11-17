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

    title_ru = models.CharField(max_length=1000, verbose_name='Заголовок')
    text_ru = models.TextField(verbose_name='Текст')
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
                            redactor_options={'buttons': ['image'],},
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
                            redactor_options={'buttons': ['image'],},
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

    def __unicode__(self):
        return self.name


class RulesOfIncomingKy(models.Model):
    class Meta:
        verbose_name = 'Келүү эреже'
        verbose_name_plural = 'Келүү эреже'

    image = models.ImageField(upload_to=image_upload_to, verbose_name='Сүрөт', null=True)
    title_ky = models.CharField(max_length=1000, verbose_name='Аталыш')
    text_ky = RedactorField(verbose_name='Баяндоо',
                            upload_to=image_upload_to,
                            redactor_options={'buttons': ['image'],},
                            allow_image_upload=True,
                            allow_file_upload=True)
    translit = models.OneToOneField(RulesOfIncoming)

    def save(self, *args, **kwargs):
        super(RulesOfIncomingKy, self).save()
        rules_of_incoming = RulesOfIncoming.objects.get(id=self.translit_id)
        rules_of_incoming.translit_id = self.id
        rules_of_incoming.save()

    def __unicode__(self):
        return self.title_ky


class RulesOfMigration(models.Model):
    class Meta:
        verbose_name = 'торговля людьми'
        verbose_name_plural = 'торговля людьми'

    image = models.ImageField(upload_to=image_upload_to, verbose_name='Иконка')
    title_ru = models.CharField(max_length=1000, verbose_name='Заголовок')
    text_ru = RedactorField(verbose_name='Баяндоо',
                            upload_to=image_upload_to,
                            redactor_options={'buttons': ['image'],},
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
                            redactor_options={'buttons': ['image'],},
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
        verbose_name_plural = 'Вопросы и ответы'

    question_ru = models.TextField(verbose_name='Вопрос')
    answer_ru = models.TextField(verbose_name='Ответ')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    translit = models.OneToOneField('FAQky', null=True)

    def __unicode__(self):
        return self.question_ru


class FAQky(models.Model):
    class Meta:
        verbose_name = 'суроо жана жооп'
        verbose_name_plural = 'суроо жана жооп'

    translit = models.OneToOneField(FAQ)
    question_ky = models.TextField(verbose_name='Суроо')
    answer_ky = models.TextField(verbose_name='Жооп')

    def save(self, *args, **kwargs):
        super(FAQky, self).save()
        faq = FAQ.objects.get(id=self.translit_id)
        faq.translit_id = self.id
        faq.save()


class CountryHotline(models.Model):
    class Meta:
        verbose_name = 'горячую линию'
        verbose_name_plural = 'Горячие линии'

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
    text_ru = models.TextField(verbose_name='Описание')
    phone_number = models.CharField(max_length=100, verbose_name='Номер телефона')

    def __unicode__(self):
        return self.title_ru
