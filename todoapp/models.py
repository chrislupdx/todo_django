from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=250)
	body = models.TextField()

	def __str__(self):
		return self.title
