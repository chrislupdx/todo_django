from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
from django.forms import ModelForm


class Todo(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.CharField(max_length=250, null=True, blank=True)
	finished = models.BooleanField(default=False)
	create_date = models.DateTimeField(default=datetime.now())

	def __str__(self):
		return self.body
