from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404, render_to_response
from django.template import Context, loader, RequestContext

from siteuser.models import *
from behaviour.models import *
from points.models import *


def r(request):
	"Total accumulated points of a student"
	siteuser = request.GET.get("name")
	s = Siteuser.objects.filter(name=siteuser)[0]
	b = Behaviour.objects.filter(bid=bid)[0]
	p = None
	try:
		p = Points.objects.filter(
			siteuser = s.pk,
		)
	except:
		print "Points could not be read"

	d = {"points": p}
	return render_to_response('po_l.html', d, context_instance = RequestContext(request) )

def c(request):
	"""Create function for points"""
	siteuser = request.GET.get("name")
	bid = request.GET.get("bid")
	s = Siteuser.objects.filter(name=siteuser)[0]
	b = Behaviour.objects.filter(bid=bid)[0]
	p = None
	try:
		p = Points.objects.create(
			siteuser = s.pk,
			points = b.points
		)
	except:
		print "Points could not be created"

	d = {"points": p}
	return render_to_response('po_c.html', d, context_instance = RequestContext(request) )
