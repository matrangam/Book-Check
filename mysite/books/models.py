from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
	tag = models.CharField(max_length=25)
	def __unicode__(self):
		return self.tag

class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    quantity = models.IntegerField()
    description = models.TextField(max_length=500)
    check_date = models.DateTimeField(default=None, blank=True, null=True)
    
    users = models.ManyToManyField(User, blank=True, null=True)
    topic = models.ManyToManyField('Topic')
    
    def __unicode__(self):
        return self.title
