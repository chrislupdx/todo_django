from django.forms import ModelForm
from .models import Todo
from django import forms
from django.template import Template

class Todoform(forms.ModelForm):
	class Meta:
		model = Todo
		fields = ['body']