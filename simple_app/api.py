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


class NewsKgResource(ModelResource):
    class Meta:
        queryset = NewsKg.objects.all()
        resource_name = 'news_kg'
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


class RulesOfIncomingResourceKg(ModelResource):
    country = fields.ForeignKey(CountryEAESResource, 'country', full=True, null=True)

    class Meta:
        queryset = RulesOfIncomingKgEAES.objects.all()
        authorization = Authorization()
        resource_name = 'rules_of_incoming_eaes_kg'

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


class RulesOfIncomingResource1Kg(ModelResource):
    country = fields.ForeignKey(CountryResource, 'country', full=True, null=True)

    class Meta:
        queryset = RulesOfIncomingKg.objects.all()
        authorization = Authorization()
        resource_name = 'rules_of_incoming_kg'

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


class RulesOfMigrationResourceKg(ModelResource):
    class Meta:
        queryset = RulesOfMigrationKg.objects.all()
        authorization = Authorization()
        resource_name = 'human_traffic_kg'


class RFResource(ModelResource):
    class Meta:
        queryset = RF.objects.all()
        authorization = Authorization()
        resource_name = 'rf'


class RFKGResource(ModelResource):
    class Meta:
        queryset = RFKG.objects.all()
        authorization = Authorization()
        resource_name = 'rf_kg'


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


class HotlineResourceKg(ModelResource):
    country = fields.ForeignKey(CountryHotlineResource, 'country', full=True, null=True)

    class Meta:
        queryset = HotlineKG.objects.all()
        authorization = Authorization()
        resource_name = 'hotline_kg'
        filtering = {
            'country': ALL_WITH_RELATIONS
        }


class FaqResource(ModelResource):
    class Meta:
        queryset = FAQ.objects.all()
        authorization = Authorization()
        resource_name = 'faq'


class FaqKgResource(ModelResource):
    class Meta:
        queryset = FAQKG.objects.all()
        authorization = Authorization()
        resource_name = 'faq_kg'
