from django.contrib import admin
from .models import *


# Register your models here.
class RulesOfEAESCountry(admin.StackedInline):
    model = RulesOfIncomingEAES
    fields = 'title_ru text_ru'.split()
    extra = 1


class RulesOfEAESCountryKG(admin.StackedInline):
    model = RulesOfIncomingKgEAES
    fields = 'title_ru text_ru'.split()
    extra = 1


class NewsAdmin(admin.ModelAdmin):
    list_display = '__unicode__ icon created_at updated_at'.split()
    fields = 'title_ru image text_ru created_at updated_at'.split()
    readonly_fields = 'created_at updated_at'.split()
    list_filter = 'updated_at'.split()

    def icon(self, obj):
        return '<img src="%s" style = "width:50px; height=50px;" />' % obj.image.url

    icon.allow_tags = True


class RulesOfEAESAdmin(admin.ModelAdmin):
    list_display = 'country icon'.split()
    inlines = [RulesOfEAESCountry, RulesOfEAESCountryKG]

    def icon(self, obj):
        return '<img src="%s" style = "width:50px; height=50px;" />' % obj.image.url

    icon.allow_tags = True


class RulesOfIncomingInline(admin.StackedInline):
    model = RulesOfIncoming
    fields = 'title_ru text_ru'.split()
    extra = 1


class RulesOfIncomingKgInline(admin.StackedInline):
    model = RulesOfIncomingKg
    fields = 'title_ru text_ru'.split()
    extra = 1


class RulesOfIncomingAdmin(admin.ModelAdmin):
    class Meta:
        model = CountryAll

    list_display = 'country icon'.split()
    inlines = [RulesOfIncomingInline, RulesOfIncomingKgInline]

    def icon(self, obj):
        return '<img src="%s" style = "width:50px; height=50px;" />' % obj.image.url

    icon.allow_tags = True


class EmploymentInline(admin.StackedInline):
    model = Employment
    extra = 1


class CountriesAdmin(admin.ModelAdmin):
    class Meta:
        model = Countries

    list_display = 'country icon'.split()
    inlines = [EmploymentInline]

    def icon(self, obj):
        return '<img src="%s" style = "width:50px; height=50px;" />' % obj.image.url

    icon.allow_tags = True


class FAQAdmin(admin.ModelAdmin):
    list_display = '__unicode__ answer_ru created_at updated_at'.split()
    fields = 'question_ru answer_ru created_at updated_at'.split()
    readonly_fields = 'created_at updated_at'.split()
    list_filter = 'updated_at'.split()


class HotlineAdmin(admin.StackedInline):
    model = Hotline
    fields = 'title_ru phone_number'.split()
    extra = 1


class HotlineKgAdmin(admin.StackedInline):
    model = HotlineKG
    fields = 'title_ru phone_number'.split()
    extra = 1


class CountryAdmin(admin.ModelAdmin):
    list_display = 'country image_img'.split()

    def image_img(self, obj):
        return '<img src="%s" style = "width:50px; height=50px;" />' % obj.image.url

    image_img.allow_tags = True
    inlines = [HotlineAdmin, HotlineKgAdmin]


class RfAdmin(admin.ModelAdmin):
    list_display = 'icon title_ru'.split()

    def icon(self, obj):
        return '<img src="%s" style = "width:50px; height=50px;" />' % obj.image.url

    icon.allow_tags = True


class RulesOfMigationAdmin(admin.ModelAdmin):
    list_display = 'icon title_ru'.split()

    def icon(self, obj):
        return '<img src="%s" style = "width:50px; height=50px;" />' % obj.image.url

    icon.allow_tags = True


admin.site.register(Country, RulesOfEAESAdmin)
admin.site.register(Countries, CountriesAdmin)
admin.site.register(CountryAll, RulesOfIncomingAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(NewsKg, NewsAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(FAQKG, FAQAdmin)
admin.site.register(CountryHotline, CountryAdmin)
admin.site.register(RulesOfMigration, RulesOfMigationAdmin)
admin.site.register(RulesOfMigrationKg, RulesOfMigationAdmin)
admin.site.register(RF, RfAdmin)
admin.site.register(RFKG, RfAdmin)
