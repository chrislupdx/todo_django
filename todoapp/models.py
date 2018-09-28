from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class Todo(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.body
		
class Todoform(ModelForm):
    class Meta:
        model = Todo
        fields = ['body']
