
# myapp/api.py

from tastypie import authorization
from tastypie_mongoengine import resources
# from test_app import documents

from points.models import *

class PointsResource(resources.MongoEngineResource):
	class Meta:
		queryset = Points.objects.all()
		allowed_methods = ('get', 'post', 'put', 'delete')
		# authorization = authorization.Authorization()
		resource_name = 'points'

