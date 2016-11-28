from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.constants import ALL_WITH_RELATIONS, ALL
from tastypie.resources import ModelResource

from newapp.models import Region, NKO, NKOKG


class RegionResource(ModelResource):
    class Meta:
        queryset = Region.objects.all()
        resource_name = 'region'
        filtering = {
            'id': ALL_WITH_RELATIONS,
            'name': ALL
        }


class NkoResource(ModelResource):

    region = fields.ForeignKey(RegionResource, 'region', full=True, null=True)

    class Meta:
        queryset = NKO.objects.all()
        authorization = Authorization()
        resource_name = 'nko'
        filtering = {
            'region': ALL_WITH_RELATIONS
        }


class NkoResourceKg(ModelResource):

    region = fields.ForeignKey(RegionResource, 'region', full=True, null=True)

    class Meta:
        queryset = NKOKG.objects.all()
        authorization = Authorization()
        resource_name = 'nko_kg'
        filtering = {
            'region': ALL_WITH_RELATIONS
        }
