from django.contrib import admin
from .models import *


# Register your models here.
class RulesOfEAESCountry(admin.StackedInline):
    model = RulesOfIncomingEAES
    fields = 'title_ru text_ru'.split()
    extra = 1


class NewsAdmin(admin.ModelAdmin):
    list_display = '__unicode__ created_at updated_at'.split()
    fields = 'title_ru text_ru created_at updated_at'.split()
    readonly_fields = 'created_at updated_at'.split()
    list_filter = 'updated_at'.split()


class RulesOfEAESAdmin(admin.ModelAdmin):
    list_display = 'country'.split()
    inlines = [RulesOfEAESCountry]


class RulesOfIncomingInline(admin.StackedInline):
    model = RulesOfIncoming
    fields = 'title_ru text_ru'.split()
    extra = 1


class RulesOfIncomingAdmin(admin.ModelAdmin):
    class Meta:
        model = CountryAll

    list_display = 'country'.split()
    inlines = [RulesOfIncomingInline]


class EmploymentInline(admin.StackedInline):
    model = Employment
    extra = 1


class CountriesAdmin(admin.ModelAdmin):
    class Meta:
        model = Countries

    list_display = 'country'.split()
    inlines = [EmploymentInline]


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


class HotlineAdmin(admin.ModelAdmin):
    list_display = '__unicode__ phone_number'.split()
    fields = 'phone_number title_ru text_ru'.split()


admin.site.register(Country, RulesOfEAESAdmin)
admin.site.register(Countries, CountriesAdmin)
admin.site.register(CountryAll, RulesOfIncomingAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(Hotline, HotlineAdmin)
admin.site.register(RulesOfMigration)
admin.site.register(RF)
