
# myapp/api.py

from tastypie.authorization import Authorization
from tastypie_mongoengine import *

from points.models import *

class PointsResource(resources.MongoEngineResource):
	# siteuser = fields.ReferenceField(to='pysite.siteuser.api.resources.PersonResource', attribute='person', full=True)
	siteuser = fields.ReferenceField(to='siteuser.api.SiteuserResource', attribute='siteuser', full=False)
	# siteuser = fields.ReferenceField(to='siteuser.api.SiteuserResource', attribute='pk', full=False)

	class Meta:
		queryset = Points.objects.all()
		allowed_methods = ('get', 'post', 'put', 'delete')
		authorization = Authorization()
		resource_name = 'points'

