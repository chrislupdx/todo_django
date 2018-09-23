from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse, HttpRequest
from .models import Todo
from . import views
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, JsonResponse

def index(request):
	todo = Todo.objects.all()
	context = {'todo':todo}
	return render(request,'todoapp/index.html', context)

def add_todo(request):
	todo = Todo.objects.all()
	add = request.POST['add_todo']
	return render(request)