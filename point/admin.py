from django.contrib import admin
from tastypie.models import ApiKey, ApiAccess

from .models import Embassy, Consulate, DiasporaKG
from .models import CountriesAll, Diaspora
from django.contrib.auth.models import Group, User

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.unregister(ApiKey)


# Register your models here.


class DiasporaInline(admin.StackedInline):
    model = Diaspora
    extra = 1


class DiasporaKGInline(admin.StackedInline):
    model = DiasporaKG
    extra = 1


class CountriesDiasporaAdmin(admin.ModelAdmin):
    class Meta:
        model = CountriesAll

    list_display = 'country icon'.split()
    inlines = [DiasporaInline,DiasporaKGInline]

    def icon(self, obj):
        return '<img src="%s" style = "width:50px; height=50px;" />' % obj.image.url

    icon.allow_tags = True


class ConsultInline(admin.StackedInline):
    model = Consulate
    fields = 'region address map_link phone_number'.split()
    extra = 1


class EmbassyAdmin(admin.ModelAdmin):
    list_display = 'country icon phone_number address'.split()
    fields = 'country image phone_number map_link site address fax'.split()
    inlines = [ConsultInline]

    def icon(self, obj):
        return '<img src="%s" style = "width:50px; height=50px;" />' % obj.image.url

    icon.allow_tags = True


admin.site.register(Embassy, EmbassyAdmin)
admin.site.register(CountriesAll, CountriesDiasporaAdmin)
