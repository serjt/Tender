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


class RulesOfIncoming(models.Model):
    class Meta:
        verbose_name = 'правило пребывания'
        verbose_name_plural = 'Правила пребывания'

    image = models.ImageField(upload_to=image_upload_to, verbose_name='Иконка')
    title_ru = models.CharField(max_length=1000, verbose_name='Заголовок')
    text_ru = RedactorField(verbose_name='Текст',
                            upload_to=image_upload_to,
                            redactor_options={'buttons': ['image'],},
                            allow_image_upload=True,
                            allow_file_upload=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    translit = models.OneToOneField('RulesOfIncomingKy', null=True)

    def __unicode__(self):
        return self.title_ru

    @staticmethod
    def autocomplete_search_fields():
        return 'title_ru'


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
        verbose_name = 'правило выезда'
        verbose_name_plural = 'Правила выезда'

    image = models.ImageField(upload_to=image_upload_to, verbose_name='Иконка')
    title_ru = models.CharField(max_length=1000, verbose_name='Заголовок')
    text_ru = RedactorField(verbose_name='Баяндоо',
                            upload_to=image_upload_to,
                            redactor_options={'buttons': ['image'],},
                            allow_image_upload=True,
                            allow_file_upload=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    translit = models.OneToOneField('RulesOfMigrationKy', null=True)

    def __unicode__(self):
        return self.title_ru

    @staticmethod
    def autocomplete_search_fields():
        return 'title_ru'


class RulesOfMigrationKy(models.Model):
    class Meta:
        verbose_name = 'Сыртка чыгуу эреже'
        verbose_name_plural = 'Сыртка чыгуу эреже'
    image = models.ImageField(upload_to=image_upload_to, verbose_name='Сүрөт', null=True)
    title_ky = models.CharField(max_length=1000, verbose_name='Аталыш')
    text_ky = RedactorField(verbose_name='Баяндоо',
                            upload_to=image_upload_to,
                            redactor_options={'buttons': ['image'],},
                            allow_image_upload=True,
                            allow_file_upload=True)
    translit = models.OneToOneField(RulesOfMigration)

    def save(self, *args, **kwargs):
        super(RulesOfMigrationKy, self).save()
        rules_of_migration = RulesOfMigration.objects.get(id=self.translit_id)
        rules_of_migration.translit_id = self.id
        rules_of_migration.save()

    def __unicode__(self):
        return self.title_ky


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

    def save(self, *args,**kwargs):
        super(FAQky,self).save()
        faq = FAQ.objects.get(id=self.translit_id)
        faq.translit_id = self.id
        faq.save()


class Hotline(models.Model):
    class Meta:
        verbose_name = 'горячую линию'
        verbose_name_plural = 'Горячие линии'

    title_ru = models.CharField(max_length=1000, verbose_name='Название горячей линии')
    text_ru = models.TextField(verbose_name='Описание')
    phone_number = models.CharField(max_length=100, verbose_name='Номер телефона')
    translit = models.OneToOneField('HotlineKy',null=True)

    def __unicode__(self):
        return self.title_ru


class HotlineKy(models.Model):
    class Meta:
        verbose_name_plural = 'hotline'

    translit = models.OneToOneField(Hotline, null=True)
    title_ky = models.CharField(max_length=1000, verbose_name='Hotline')
    text_ky = models.TextField(verbose_name='Баяндоо')

    def save(self, *args,**kwargs):
        super(HotlineKy,self).save()
        hotline = Hotline.objects.get(id = self.translit_id)
        hotline.translit_id = self.id
        hotline.save()
