from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404, render_to_response
from django.template import Context, loader, RequestContext

from attendance.models import *
from siteuser.models import *


def c(request):
	"""This will update the attendance of a student"""
	stud = request.GET.get("name")
	s = Siteuser.objects.filter(name=stud).get(0)
	try:
		cr = Attendance.objects.create(siteuser=s.pk)
	except:
		print "Couldn't create attendance"

	d = {"siteuser": s}
	return render_to_response('att_c.html', d, context_instance=RequestContext(request) )

def r(request):
	"""This will update the attendance of a student"""
	stud = request.GET.get("name")
	s = Siteuser.objects.filter(name=stud)[0]
	att = Attendance.objects.filter(siteuser=s.pk)
	d = {"att": att}
	return render_to_response('att_r.html', d, context_instance=RequestContext(request) )

