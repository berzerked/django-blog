from django.db import models

#Django models- basically a database. 
#Each class is a table and each variable within a class is a column.

class Post(models.Model):
	title =  models.CharField(max_length=140)
	body = models.TextField()
	date = models.DateTimeField()

	def __str__(self):
		return self.title