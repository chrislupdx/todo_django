from django.urls import path, include
from . import views

app_name = 'todoapp' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    path('add_todo', views.add_todo, name='add_todo'),
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete_todo'),
    path('finished_task/<int:pk>/', views.finished_task, name='finished_task'),
    path('todo_display/', views.todo_display, name='todo_display'),

]