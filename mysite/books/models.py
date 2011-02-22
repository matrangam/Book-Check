from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=500)
	author = models.CharField(max_length=100)
	quantity = models.IntegerField()
	topic = models.ForeignKey(Topic)
	description = models.TextField(max_length=500)
	def __unicode__(self):
		return self.title




class Topic(models.Model):
	tag = models.CharField(max_length=25)
	def __unicode__(self):
		return self.tag

