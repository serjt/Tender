from django.contrib import admin
from .models import *
# Register your models here.


class StoryAdmin(admin.ModelAdmin):
    fields = 'user title text publish created_at updated_at'.split()
    readonly_fields = 'created_at updated_at'.split()
    list_display = '__unicode__ publish'.split()


class CommentInline(admin.StackedInline):
    model = Comment
    fields = 'user answer created_at updated_at'.split()
    readonly_fields = 'created_at updated_at'.split()
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fields = 'user question created_at updated_at'.split()
    readonly_fields = 'created_at updated_at'.split()
    inlines = [CommentInline]

admin.site.register(Story,StoryAdmin)
admin.site.register(Question,QuestionAdmin)