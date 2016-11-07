from tastypie.authorization import Authorization

from .models import *
from tastypie.resources import ModelResource,ALL,ALL_WITH_RELATIONS
from tastypie import fields


class EmbassyResource(ModelResource):
    class Meta:
        queryset = Embassy.objects.all()
        resource_name = 'embassy'
        filtering = {
            'id':ALL_WITH_RELATIONS,
            'country':ALL

        }


class CountryDiasporaResource(ModelResource):
    class Meta:
        queryset = CountriesAll.objects.all()
        resource_name = 'country_diaspora'
        filtering = {
            'id': ALL_WITH_RELATIONS,
            'country': ALL

        }


class RulesOfIncomingResource3(ModelResource):
    country = fields.ForeignKey(CountryDiasporaResource, 'country', full=True, null=True)

    class Meta:
        queryset = Diaspora.objects.all()
        authorization = Authorization()
        resource_name = 'diaspora'

        filtering = {
            'country': ALL_WITH_RELATIONS
        }


class ConsulateResource(ModelResource):

    embassy = fields.ForeignKey(EmbassyResource,'embassy',full=True,null=True)

    class Meta:
        queryset = Consulate.objects.all()
        resource_name = 'consulate'
        filtering = {
            'embassy':ALL_WITH_RELATIONS,
        }