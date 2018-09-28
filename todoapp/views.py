from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse, HttpRequest
from .models import Todo
from . import views
from django import forms
from .forms import Todoform
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, JsonResponse

def index(request):
	todo_list = Todo.objects.all()
	context = {'todo':todo_list}
	return render(request,'todoapp/index.html', context)

def add_todo(request):
	if request.method == 'POST':
		form = Todoform(request.POST)
		if form.is_valid():
			todo = form.save(commit=False)
			todo.save()
			return redirect('lfw:index')
	else:

		form = Todoform()
	context = {'form': form}
	return render(request, 'lfw/index.html', context)

def todo_display(request):
	todo = Todo.objects.all()
	context = {'todo' :todo}
	return render(request,'lfw/todo_display.html', context)

