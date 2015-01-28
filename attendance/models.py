from django.db import models

# Create your models here.

from siteuser.models import Siteuser

# from djangotoolbox.fields import ListField
# from djangotoolbox.fields import EmbeddedModelField

from mongoengine import *
import datetime

# from django.db.models.loading import cache as model_cache
# if not model_cache.loaded:
# 	model_cache.get_models()

# class Attendance(models.Model):
class Attendance(Document):
	# siteuser = EmbeddedModelField("Siteuser")
	siteuser = ReferenceField(Siteuser)
	date = DateTimeField(default=datetime.datetime.now)
	meta = {'allow_inheritance': True}

