from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('attendance.views',
	# Examples:
	# url(r'^$', 'pysite.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	#A
	url(r'c', 'c', name="attendance_create"),
	url(r'r', 'r', name="attendance_list"),

	url(r'', 'index'),

    #A-
)
