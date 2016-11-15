from django.contrib import admin
from tastypie.models import ApiKey, ApiAccess

from .models import Embassy,Consulate
from .models import CountriesAll,Diaspora
from django.contrib.auth.models import Group,User

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.unregister(ApiKey)
# Register your models here.


class DiasporaInline(admin.StackedInline):
    model = Diaspora
    extra = 1


class CountriesDiasporaAdmin(admin.ModelAdmin):
    class Meta:
        model = CountriesAll
    list_display = 'country'.split()
    inlines = [DiasporaInline]


class ConsultInline(admin.StackedInline):
    model = Consulate
    fields = 'region address phone_number'.split()
    extra = 1


class EmbassyAdmin(admin.ModelAdmin):
    list_display = '__unicode__ phone_number address'.split()
    fields = 'country phone_number site address fax'.split()
    inlines = [ConsultInline]

admin.site.register(Embassy,EmbassyAdmin)
admin.site.register(CountriesAll, CountriesDiasporaAdmin)
