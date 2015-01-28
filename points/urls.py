from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('points.views',
	# Examples:
	# url(r'^$', 'pysite.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	#A
	url(r'c', 'c', name="points_create"),
	url(r'r', 'r', name="points_list"),

	url(r'', 'index'),

    #A-
)
