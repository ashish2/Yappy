# siteuser/api.py

from tastypie.resources import ModelResource
from tastypie_mongoengine import fields, resources

from test_app import documents
from siteuser.models import *


class SiteuserResource(resources.MongoEngineResource):
	class Meta:
		queryset = documents.Siteuser.objects.all()

		allowed_methods = ('get', 'post', 'put', 'patch', 'delete')
		authorization = tastypie_authorization.Authorization()
		paginator_class = paginator.Paginator

		resource_name = 'siteuser'

