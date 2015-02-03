from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404, render_to_response
from django.template import Context, loader, RequestContext

from siteuser.models import *
from behaviour.models import *
from points.models import *


def r(request):
	"""Total accumulated points of a student"""
	siteuser = request.GET.get("name")
	siteuser_o = Siteuser.objects.filter(name=siteuser).get(0)
	p = None
	try:
		points_o = Points.objects.filter(siteuser=siteuser_o.pk)
	except:
		print "Points could not be read"

	dic = {"points": points_o}
	return render_to_response('po_l.html', dic, context_instance = RequestContext(request) )

def c(request):
	"""Create function for points"""
	siteuser = request.GET.get("name")
	bid = request.GET.get("bid")
	
	siteuser_o = Siteuser.objects.filter(name=siteuser)[0]
	beh_o = Behaviour.objects.filter(bid=bid)[0]
	p = None
	try:
		points_o = Points.objects.create(
			siteuser = siteuser_o.pk,
			points = beh_o.points
		)
	except:
		print "Points could not be created"

	dic = {"points": points_o}
	return render_to_response('po_c.html', dic, context_instance = RequestContext(request) )
