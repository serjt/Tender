from django.contrib import admin
from .models import Embassy,Consulate
# Register your models here.


class ConsultInline(admin.StackedInline):
    model = Consulate
    fields = 'region address phone_number'.split()
    extra = 1


class EmbassyAdmin(admin.ModelAdmin):
    list_display = '__unicode__ phone_number address'.split()
    fields = 'country phone_number site address fax'.split()
    inlines = [ConsultInline]

admin.site.register(Embassy,EmbassyAdmin)
