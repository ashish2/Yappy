from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404, render_to_response
from django.template import Context, loader, RequestContext

from behaviour.models import *

def c(request):
	"""Create function for Behaviour"""
	bid = request.GET.get("bid")
	name = request.GET.get("name")
	points = request.GET.get("points")

	try:
		b, cr = Behaviour.objects.get_or_create(
			bid = bid,
			name = name,
			points = points
		)
	except:
		print "Behaviour coultdn't be created"

	d = {"behaviour": b}
	return render_to_response('beh_c.html', d, context_instance=RequestContext(request) )

def r(request):
	"""Read function for Behaviour"""
	b = Behaviour.objects.all()
	d = {"behaviour": b}
	return render_to_response('beh_r.html', d, context_instance=RequestContext(request) )
