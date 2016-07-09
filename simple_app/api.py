from .models import *
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS


class RulesOfIncomingKyResource(ModelResource):
    class Meta:
        queryset = RulesOfIncomingKy.objects.all()
        resource_name = 'rules_of_incoming_ky'


class RulesOfIncomingResource(ModelResource):
    translit = fields.ToOneField(RulesOfIncomingKyResource, 'translit', full=True, null=True)

    class Meta:
        queryset = RulesOfIncoming.objects.all()
        authorization = Authorization()
        resource_name = 'rules_of_incoming'


class RulesOfMigrationKyResource(ModelResource):
    class Meta:
        queryset = RulesOfMigrationKy.objects.all()
        resource_name = 'rules_of_migration_ky'


class RulesOfMigrationResource(ModelResource):
    translit = fields.ToOneField(RulesOfMigrationKyResource, 'translit', full=True, null=True)

    class Meta:
        queryset = RulesOfMigration.objects.all()
        authorization = Authorization()
        resource_name = 'rules_of_migration'


class HotlineKyResource(ModelResource):
    class Meta:
        queryset = HotlineKy.objects.all()
        resource_name = 'hotline_ky'


class HotlineResource(ModelResource):
    translit = fields.ToOneField(HotlineKyResource, 'translit', full=True, null=True)

    class Meta:
        queryset = Hotline.objects.all()
        authorization = Authorization()
        resource_name = 'hotline'


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
