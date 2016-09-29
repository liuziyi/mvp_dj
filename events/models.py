from django.db import models

class Event(models.Model):
	title = models.CharField(max_length=120)
	start_date = models.DateField(null=True, blank=True)
	end_date = models.DateField(null=True, blank=True)
	venue = models.CharField(max_length=120, null=True, blank=True)
	deadline = models.DateField(null=True, blank=True)
	link = models.URLField(null=True, blank=True)

	class Meta:
		ordering = ['start_date']

	def __unicode__(self):
		return self.title
