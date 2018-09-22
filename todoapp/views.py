from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse, HttpRequest

from . import views
from django.shortcuts import render


def index(request):
    return render(request,'todo/index.html')

def add_todo(request):
	todo = Todo.objects.all()
	add = request.POST['add_todo']
	return render(request)