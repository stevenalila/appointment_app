from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class Appointment(models.Model):
	user = models.ForeignKey('auth.User')
	name = models.CharField(max_length=255)
	task = models.CharField(max_length=255)
	datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
	status = models.BooleanField()
	created = models.DateTimeField(auto_now=True, auto_now_add=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	def get_absolute_url(self):
		return reverse('edit', kwargs={'id': self.id})

	def get_delete_url(self):
		return reverse('delete', kwargs={'id': self.id})
