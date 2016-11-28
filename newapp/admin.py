from django.contrib import admin
from .models import Region, NKO, NKOKG


# Register your models here.

class NkoInline(admin.StackedInline):
    model = NKO
    fields = 'title_ru text_ru manager address phone_number phone_number_1 mail'.split()
    extra = 1


class NkoKGInline(admin.StackedInline):
    model = NKOKG
    fields = 'title_ru text_ru manager address phone_number phone_number_1 mail'.split()
    extra = 1


class RegionAdmin(admin.ModelAdmin):
    class Meta:
        model = Region

    list_display = 'name'.split()
    inlines = [NkoInline,NkoKGInline]


admin.site.register(Region, RegionAdmin)
