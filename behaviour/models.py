from django.db import models

# Create your models here.
from mongoengine import *

class Behaviour(Document):
	bid = StringField(max_length=50)
	name = StringField(max_length=50)
	points = IntField()

