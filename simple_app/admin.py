from django.contrib import admin
from .models import *


# Register your models here.
class RulesOfEAESCountry(admin.StackedInline):
    model = RulesOfIncomingEAES
    fields = 'title_ru text_ru'.split()
    extra = 1


class NewsAdmin(admin.ModelAdmin):
    list_display = '__unicode__ created_at updated_at'.split()
    fields = 'title_ru image text_ru created_at updated_at'.split()
    readonly_fields = 'created_at updated_at'.split()
    list_filter = 'updated_at'.split()
    #
    # def icon(self,obj):
    #     return '<img src="%s" style = "width:50px; height=50px;" />' % obj.image.url
    #
    # icon.allow_tags = True


class RulesOfEAESAdmin(admin.ModelAdmin):
    list_display = 'country icon'.split()
    inlines = [RulesOfEAESCountry]

    def icon(self, obj):
        return '<img src="%s" style = "width:50px; height=50px;" />' % obj.image.url

    icon.allow_tags = True


class RulesOfIncomingInline(admin.StackedInline):
    model = RulesOfIncoming
    fields = 'title_ru text_ru'.split()
    extra = 1


class RulesOfIncomingAdmin(admin.ModelAdmin):
    class Meta:
        model = CountryAll

    list_display = 'country icon'.split()
    inlines = [RulesOfIncomingInline]

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


class HotlineAdmin(admin.StackedInline):
    model = Hotline
    fields = 'title_ru text_ru phone_number'.split()
    extra = 1


class CountryAdmin(admin.ModelAdmin):
    list_display = 'country image_img'.split()

    def image_img(self, obj):
        return '<img src="%s" style = "width:50px; height=50px;" />' % obj.image.url

    image_img.allow_tags = True
    inlines = [HotlineAdmin]


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
admin.site.register(FAQ, FAQAdmin)
admin.site.register(CountryHotline, CountryAdmin)
admin.site.register(RulesOfMigration, RulesOfMigationAdmin)
admin.site.register(RF, RfAdmin)
