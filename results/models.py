from django.db import models

class Result(models.Model):
	event = models.CharField(max_length=120)
	date = models.DateField()

	class Meta:
		ordering = ['date']

	def __unicode__(self):
		return self.event

class ResultDetail(models.Model):
	event = models.ForeignKey(Result)
	category = models.CharField(max_length=120, null=True, blank=True)
	title = models.CharField(max_length=120, null=True, blank=True)
	name_of_winner = models.CharField(max_length=120, null=True, blank=True)

	def __unicode__(self):
		return self.category 