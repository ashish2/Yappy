from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from mongoengine import *

class Siteuser(Document):
	name = StringField(max_length=120)
	age = IntField()
	standard = IntField()

