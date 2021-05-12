from django.shortcuts import render , redirect
from .models import Todo
# Create your views here.

def Index(request):
    todos = Todo.objects.filter(completed=False) # Read
    todos_completed = Todo.objects.filter(completed=True) # Read
    template = 'index.html'
    if request.method == 'POST':
        task = request.POST['todo_task']
        Todo.objects.create(task_name=task) # Create
    return render(request,template,{
        'all_todos':todos,
        'todos_completed':todos_completed
    })



def Completed(request,id):
    todo = Todo.objects.get(id=id) # single instance of model
    todo.completed = True # Updated
    todo.save()
    return redirect('/')

def NonCompleted(request,id):
    todo = Todo.objects.get(id=id) # single instance of model
    todo.completed = False # Updated
    todo.save()
    return redirect('/')

def Delete(request,id):
    todo = Todo.objects.get(id=id) # Delete
    todo.delete()
    return redirect('/')