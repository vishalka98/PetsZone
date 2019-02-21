from django.db import models


# Create your models here.

class GuestEmail(models.Model):
	email     = models.EmailField(default=True)
	active = models.BooleanField(default=True)
	update = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.email