# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Story(models.Model):
    class Meta:
        verbose_name = 'историю из жизни'
        verbose_name_plural = 'Истории из жизни'
    user = models.ForeignKey(User,verbose_name='Пользователь')
    title = models.CharField(max_length=100,verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    publish = models.BooleanField(verbose_name='Опубликовать')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания',null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения',null=True)

    def __unicode__(self):
        return self.title


class Question(models.Model):
    class Meta:
        verbose_name = 'вопрос и ответ'
        verbose_name_plural = 'Вопросы и ответы'
    user = models.ForeignKey(User,verbose_name='Пользователь')
    question = models.TextField(verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания',null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения',null=True)

    def __unicode__(self):
        return self.question


class Comment(models.Model):
    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'

    question = models.ForeignKey(Question)
    user = models.ForeignKey(User,verbose_name='Пользователь')
    answer = models.TextField(verbose_name='Ответ')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания',null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения',null=True)

    def __unicode__(self):
        return self.answer


