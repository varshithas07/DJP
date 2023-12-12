from django.shortcuts import render,redirect
from django.urls import reverse #to tak the extension and new url should comin
from .models import Task
from .forms import TaskForm

# Create your views here.

#create
def task_create(request):
    if request.method == "POST": #checking if any thing in the form
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("tasks:task_list")) #redirecting it to  view ing the list
    else:
        form=TaskForm() #just display the empty form
    return render(request, "tasks/task_form.html", {'form':form,}) #only passing the html page

# list
def task_list(request):
   #tasks is given in forloop of html page
    tasks =Task.objects.all() #model.obejcts (all objects)
    return render(request, "tasks/task_list.html", {"tasks":tasks,})

# detail view

def task_detail(request,pk):
    task=Task.objects.get(pk=pk)
    return render(request, "tasks/task_detail.html",{"task":task,})

# update single task
def task_update(request,pk):
    task = Task.objects.get(pk=pk)
    if request.method == "POST":
        form = TaskForm(instance=task, data=request.POST) #instance=what ever fill in form is comming from task when saving requesting data from post
        if form.is_valid():
            form.save()
            return redirect(reverse("tasks:task_detail", args=[pk,]))
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/task_form.html", {"form":form,"object":task})

# delete
def task_delete(request,pk):
    task_obj = Task.objects.get(pk=pk)
    task_obj.delete()
    return redirect(reverse("tasks:task_list"))