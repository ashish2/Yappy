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



## Siteuser ##

# POST
# curl --dump-header - -H "Content-Type: application/json" -X POST --data '{ "standard": "8", "age": "40", "name": "abc"}' http://localhost:8000/api/v1/siteuser/
# curl --dump-header - -H "Content-Type: application/json" -d '{"name": "xyz", "age": 40, "standard": 9}' "http://localhost:8000/api/v1/siteuser/"

# PUT
# curl --dump-header - -H "Content-Type: application/json" -X PUT -d '{"name": "xyz", "age": 40, "standard": 10}' "http://localhost:8000/api/v1/siteuser/54cfdbae055fee144977de35/"

# PATCH
# curl --dump-header - -H "Content-Type: application/json" -X PATCH -d '{"standard": 5}' "http://localhost:8000/api/v1/siteuser/54cfdbae055fee144977de35/"


## Points ##

# POST
# POSTing related fields
# curl --dump-header - -H "Content-Type: application/json" -d '{ "points": 3, "siteuser": "/api/v1/siteuser/54c8beee055fee0e0de3a905/"}' "http://localhost:8000/api/v1/points/"

# DELETing
# curl --dump-header - -X DELETE "http://localhost:8000/api/v1/points/54d0b54a055fee14767bf161/"

