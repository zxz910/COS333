from django.db import models
from django.contrib.auth.models import User

class Thread(models.Model):
	author             = models.ForeignKey(User, null = True)
	title              = models.CharField(max_length = 150)
	pub_date           = models.DateTimeField(auto_now_add = True)
	tags               = models.ManyToManyField('Tag')
	professor_viewable = models.BooleanField()
	
class Post(models.Model):
	author   = models.ForeignKey(User, null = True)
	content  = models.CharField(max_length = 2000)
	pub_date = models.DateTimeField(auto_now_add = True)
	thread   = models.ForeignKey('Thread')
	
class Tag(models.Model):
	tag = models.CharField(max_length = 16)
