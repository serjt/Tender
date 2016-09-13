# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models import signals
from tastypie.models import create_api_key


class Story(models.Model):
    class Meta:
        verbose_name = 'историю из жизни'
        verbose_name_plural = 'Истории из жизни'

    user = models.ForeignKey(User, verbose_name='Пользователь', null=True, blank=True)
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    category = models.CharField(max_length=100)
    text = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', null=True)

    def __unicode__(self):
        return self.title


class StoryComment(models.Model):
    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'

    story = models.ForeignKey(Story)
    user = models.ForeignKey(User, verbose_name='Пользователь')
    answer = models.TextField(verbose_name='Ответ')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', null=True)

    def __unicode__(self):
        return self.answer


class Question(models.Model):
    class Meta:
        verbose_name = 'вопрос и ответ'
        verbose_name_plural = 'Вопросы и ответы'

    user = models.ForeignKey(User, verbose_name='Пользователь')
    question = models.TextField(verbose_name='Вопрос')
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', null=True)

    def __unicode__(self):
        return self.question


class Comment(models.Model):
    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'

    question = models.ForeignKey(Question)
    user = models.ForeignKey(User, verbose_name='Пользователь')
    answer = models.TextField(verbose_name='Ответ')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', null=True)

    def __unicode__(self):
        return self.answer


signals.post_save.connect(create_api_key, sender=User)
