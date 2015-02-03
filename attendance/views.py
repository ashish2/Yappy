from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404, render_to_response
from django.template import Context, loader, RequestContext

from attendance.models import *
from siteuser.models import *


def c(request):
	"""This will update the attendance of a student"""
	stud = request.GET.get("name")
	siteuser_o = Siteuser.objects.filter(name=stud).get(0)
	try:
		att_cr = Attendance.objects.create(siteuser=siteuser_o.pk)
	except:
		print "Couldn't create attendance"

	dic = {"siteuser": siteuser_o, "attendance": att_cr}
	return render_to_response('att_c.html', dic, context_instance=RequestContext(request) )

def r(request):
	"""This will update the attendance of a student"""
	stud = request.GET.get("name")
	siteuser_o = Siteuser.objects.filter(name=stud)[0]
	att_o = Attendance.objects.filter(siteuser=siteuser_o.pk)
	dic = {"att": att_o}
	return render_to_response('att_r.html', dic, context_instance=RequestContext(request) )

