from django.contrib import admin
from .models import *


# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = '__unicode__ created_at updated_at'.split()
    fields = 'title_ru text_ru created_at updated_at'.split()
    readonly_fields = 'created_at updated_at'.split()
    list_filter = 'updated_at'.split()


class FAQinline(admin.StackedInline):
    model = FAQky
    fields = 'question_ky answer_ky'.split()
    extra = 1


class FAQAdmin(admin.ModelAdmin):
    list_display = '__unicode__ answer_ru created_at updated_at'.split()
    fields = 'question_ru answer_ru created_at updated_at'.split()
    readonly_fields = 'created_at updated_at'.split()
    list_filter = 'updated_at'.split()
    inlines = [FAQinline]


class RulesOfIncomingInline(admin.StackedInline):
    model = RulesOfIncomingKy
    fields = 'image title_ky text_ky'.split()
    extra = 1


class RulesOfIncomingAdmin(admin.ModelAdmin):
    list_display = '__unicode__ created_at updated_at'.split()
    fields = 'image title_ru text_ru created_at updated_at'.split()
    readonly_fields = 'created_at updated_at'.split()
    list_filter = 'updated_at'.split()
    inlines = [RulesOfIncomingInline]


class RulesOfMigrationInline(admin.StackedInline):
    model = RulesOfMigrationKy
    fields = 'image title_ky text_ky'.split()
    extra = 1


class RulesOfMigrationAdmin(admin.ModelAdmin):
    list_display = '__unicode__ created_at updated_at'.split()
    fields = 'image title_ru text_ru created_at updated_at'.split()
    readonly_fields = 'created_at updated_at'.split()
    list_filter = 'updated_at'.split()
    inlines = [RulesOfMigrationInline]


class HotlineInline(admin.StackedInline):
    model = HotlineKy
    fields = 'title_ky text_ky'.split()
    extra = 1


class HotlineAdmin(admin.ModelAdmin):
    list_display = '__unicode__ phone_number'.split()
    fields = 'phone_number title_ru text_ru'.split()
    inlines = [HotlineInline]
admin.site.register(News, NewsAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(RulesOfIncoming,RulesOfIncomingAdmin)
admin.site.register(RulesOfMigration,RulesOfMigrationAdmin)
admin.site.register(Hotline,HotlineAdmin)
