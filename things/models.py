from django.db import models

class Thing(models.Model):
	name = models.CharField(unique=True,blank=False,max_length=30)
	description = models.TextField(max_length=100)
	quantity = models.IntegerField(min_value=0,max_value=100,blank=False)
