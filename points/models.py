from django.db import models

# Create your models here.

from siteuser.models import Siteuser
from mongoengine import *
import datetime

# This models.Model field needs to work with djangotoolbox (ATM EmbeddedModelField Not working)
# class Points(models.Model):
# This Document working with mongoengine (ATM ReferenceField working fine)
class Points(Document):
	"""This table will keep inserting & summing up rather than updating the same record"""
	# siteuser = EmbeddedModelField('Siteuser')
	siteuser = ReferenceField(Siteuser)
	points = IntField() # some points total value
	date = DateTimeField(default=datetime.datetime.now)
	
	meta = {'allow_inheritance': True}
