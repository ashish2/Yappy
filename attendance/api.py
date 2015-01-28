
# myapp/api.py
from tastypie.resources import ModelResource
from attendance.models import *


class AttendanceResource(ModelResource):
	class Meta:
		queryset = Attendance.objects.all()
		resource_name = 'attendance'

