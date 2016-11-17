from .models import *
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS


class NewsResource(ModelResource):
    class Meta:
        queryset = News.objects.all()
        resource_name = 'news'
        filtering = {
            'title_ru': ALL
        }


# class RulesOfIncomingKyResource(ModelResource):
#     class Meta:
#         queryset = RulesOfIncomingKy.objects.all()
#         resource_name = 'rules_of_incoming_ky'

class CountryEAESResource(ModelResource):
    class Meta:
        queryset = Country.objects.all()
        resource_name = 'country_eaes'
        filtering = {
            'id': ALL_WITH_RELATIONS,
            'country': ALL

        }


class RulesOfIncomingResource(ModelResource):
    country = fields.ForeignKey(CountryEAESResource, 'country', full=True, null=True)

    class Meta:
        queryset = RulesOfIncomingEAES.objects.all()
        authorization = Authorization()
        resource_name = 'rules_of_incoming_eaes'

        filtering = {
            'country': ALL_WITH_RELATIONS
        }


class CountryResource(ModelResource):
    class Meta:
        queryset = CountryAll.objects.all()
        resource_name = 'country'
        filtering = {
            'id': ALL_WITH_RELATIONS,
            'country': ALL

        }


class RulesOfIncomingResource1(ModelResource):
    country = fields.ForeignKey(CountryResource, 'country', full=True, null=True)

    class Meta:
        queryset = RulesOfIncoming.objects.all()
        authorization = Authorization()
        resource_name = 'rules_of_incoming'

        filtering = {
            'country': ALL_WITH_RELATIONS
        }


class CountriesResource(ModelResource):
    class Meta:
        queryset = Countries.objects.all()
        resource_name = 'country_employment'
        filtering = {
            'id': ALL_WITH_RELATIONS,
            'country': ALL

        }


class RulesOfIncomingResource2(ModelResource):
    country = fields.ForeignKey(CountriesResource, 'country', full=True, null=True)

    class Meta:
        queryset = Employment.objects.all()
        authorization = Authorization()
        resource_name = 'employment'

        filtering = {
            'country': ALL_WITH_RELATIONS
        }


class RulesOfMigrationResource(ModelResource):
    class Meta:
        queryset = RulesOfMigration.objects.all()
        authorization = Authorization()
        resource_name = 'human_traffic'


class RFResource(ModelResource):
    class Meta:
        queryset = RF.objects.all()
        authorization = Authorization()
        resource_name = 'rf'


class CountryHotlineResource(ModelResource):
    class Meta:
        queryset = CountryHotline.objects.all()
        resource_name = 'country_hotline'
        filtering = {
            'id': ALL_WITH_RELATIONS,
            'country': ALL
        }


class HotlineResource(ModelResource):

    country = fields.ForeignKey(CountryHotlineResource, 'country', full=True, null=True)

    class Meta:
        queryset = Hotline.objects.all()
        authorization = Authorization()
        resource_name = 'hotline'
        filtering = {
            'country': ALL_WITH_RELATIONS
        }


class FaqKyResource(ModelResource):
    class Meta:
        queryset = FAQky.objects.all()
        resource_name = 'faq_ky'


class FaqResource(ModelResource):
    translit = fields.ToOneField(FaqKyResource, 'translit', full=True, null=True)

    class Meta:
        queryset = FAQ.objects.all()
        authorization = Authorization()
        resource_name = 'faq'
