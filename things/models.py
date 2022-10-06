from django.db import models

class Thing():
	name = models.CharField()
	description = models.TextField()
	quantity = models.IntegerField()
