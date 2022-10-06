from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

class Thing(models.Model):
	name = models.CharField(unique=True,blank=False,max_length=30)
	description = models.TextField(max_length=100)
	quantity = models.IntegerField(validators=
		[MinValueValidator(0),MaxValueValidator(100)],blank=False)
