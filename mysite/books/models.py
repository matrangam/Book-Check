from django.db import models

class Topic(models.Model):
	tag = models.CharField(max_length=25)
	def __unicode__(self):
		return self.tag

class Book(models.Model):
	title = models.CharField(max_length=500)
	author = models.CharField(max_length=100)
	quantity = models.IntegerField()
	topic = models.ManyToManyField('Topic')
	description = models.TextField(max_length=500)
	
	def __unicode__(self):
		return self.title

class User(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    books = models.ManyToManyField('Book')
    def __unicode__(self):
        return self.user_name


