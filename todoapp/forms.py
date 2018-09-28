from django.forms import ModelForm
from django import forms
from .models import Todo
from django.template import Template

class Todoform(forms.ModelForm):
	class Meta:
		model = Todo
		fields = ['body']
