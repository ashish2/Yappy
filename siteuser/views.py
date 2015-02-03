from django.shortcuts import render, render_to_response

# Create your views here.

from django.template import RequestContext
from pysite.settings import *
from siteuser.models import *

def c(request):

	name = request.GET.get('name')
	age = request.GET.get('age')
	std = request.GET.get('standard')

	siteuser_o, cr = Siteuser.objects.get_or_create(name=name, age=age, standard=std)
	dic = {"siteuser": siteuser_o}
	return render_to_response('su_c.html', dic, context_instance = RequestContext(request) )


def r(request):
	name = request.GET.get('name')

	siteuser_o = Siteuser.objects.filter(name=name, age=age, standard=std).get(0)
	dic = {"siteuser": siteuser_o}
	return render_to_response('su_r.html', dic, context_instance = RequestContext(request) )

