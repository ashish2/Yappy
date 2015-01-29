from django.conf.urls import patterns, include, url
from django.contrib import admin

from attendance.models import *

#API

# from tastypie.api import Api
# from attendance.api import *

# v1_api = Api(api_name='v1')
# v1_api.register(SiteuserResource())
# v1_api.register(AttendanceResource())

#API-

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'pysite.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	#A
	url(r'^attendance/', include("attendance.urls")),
	# url(r'^site_user/', include("site_user.urls")),
	url(r'^siteuser/', include("siteuser.urls")),
	url(r'^behaviour/', include("behaviour.urls")),
	url(r'^points/', include("points.urls")),

	# Api
	# (r'^api/', include(v1_api.urls)),

	#A-
	url(r'^admin/', include(admin.site.urls)),

)


