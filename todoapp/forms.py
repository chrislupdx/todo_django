from django import forms
from django.template import Template
from .models import Todo
from django.forms import ModelForm


class Todoform(ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'body',)