"""Tender URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from tastypie.api import Api
from simple_app.api import *
from newapp.api import RegionResource,NkoResource, NkoResourceKg
from point.api import *

v1_api = Api(api_name='v1')
v1_api.register(NewsResource())
v1_api.register(NewsKgResource())
v1_api.register(RulesOfIncomingResource())
v1_api.register(RulesOfIncomingResourceKg())
v1_api.register(RulesOfMigrationResource())
v1_api.register(RulesOfMigrationResourceKg())
v1_api.register(HotlineResource())
v1_api.register(HotlineResourceKg())
v1_api.register(FaqResource())
v1_api.register(FaqKgResource())
v1_api.register(EmbassyResource())
v1_api.register(ConsulateResource())
v1_api.register(CountryResource())
v1_api.register(CountriesResource())
v1_api.register(CountryDiasporaResource())
v1_api.register(RFResource())
v1_api.register(RFKGResource())
v1_api.register(CountryEAESResource())
v1_api.register(RulesOfIncomingResource1())
v1_api.register(RulesOfIncomingResource1Kg())
v1_api.register(RulesOfIncomingResource2())
v1_api.register(RulesOfIncomingResource3())
v1_api.register(CountryHotlineResource())
v1_api.register(RegionResource())
v1_api.register(NkoResource())
v1_api.register(NkoResourceKg())
v1_api.register(DiasporaResourceKG())

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^blacklist/', 'simple_app.views.check_black_list'),
    url(r'^api/', include(v1_api.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
