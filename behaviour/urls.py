from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('behaviour.views',
	# Examples:
	# url(r'^$', 'pysite.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	#A
	url(r'c', 'c', name="behaviour_create"),
	url(r'r', 'r', name="behaviour_list"),

	# url(r'', 'index'),

    #A-
)
