# siteuser/api.py

from tastypie.resources import ModelResource
from tastypie_mongoengine import fields, resources

# import urlparse
# from tastypie.serializers import Serializer
from tastypie.authorization import Authorization

from siteuser.models import *


class SiteuserResource(resources.MongoEngineResource):
	class Meta:
		queryset = Siteuser.objects.all()

		allowed_methods = ('get', 'post', 'put', 'patch', 'delete')
		authorization = Authorization()
		# paginator_class = paginator.Paginator
		resource_name = 'siteuser'
		# serializer = urlencodeSerializer()




