from django.shortcuts import render, redirect

from .models import *
from .forms import *


def show_tasks(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {"tasks": tasks, "form": form}

    return render(request, "tasks/list.html", context)


def update_task(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect("/")
    context = {"form": form}

    return render(request, "tasks/updated_task.html", context)


def delete_task(request):
    pass

