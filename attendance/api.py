
# myapp/api.py

from tastypie import authorization
from tastypie_mongoengine import resources
# from test_app import documents

from attendance.models import *

class AttendanceResource(resources.MongoEngineResource):
	class Meta:
		queryset = Attendance.objects.all()
		allowed_methods = ('get', 'post', 'put', 'delete')
		# authorization = authorization.Authorization()
		resource_name = 'attendance'

