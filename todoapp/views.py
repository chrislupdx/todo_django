from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse, HttpRequest
from .models import Todo
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms
from .forms import Todoform
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, JsonResponse

def index(request):
	if request.user.is_authenticated:
		todo_list = Todo.objects.filter(user=request.user)
	else :
		todo_list = []
	context = {'todo':todo_list}
	return render(request,'todoapp/index.html', context)

@login_required
def add_todo(request):
	if request.method == 'POST':
		todotext = request.POST.get('todo_text')
		newtodo = Todo(body=todotext, user=request.user)
		newtodo.save()
	return redirect('todoapp:index')

def todo_display(request):
	todo = Todo.objects.all()
	context = {'todo' :todo}
	return render(request,'lfw/todo_display.html', context)

@login_required
def delete_todo(request, pk):
	todo = get_object_or_404(Todo, pk=pk)
	todo.delete()
	return redirect('todoapp:index')
	
@login_required
def finished_task(request, pk):
	todo = get_object_or_404(Todo, pk=pk)
	todo.finished = not todo.finished
	todo.save()
	return redirect('todoapp:index')