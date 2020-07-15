from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone
from django.utils.timezone import now, localtime

from todolist_app.models import Tasklist
from todolist_app.forms import Taskform, Contactform
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from datetime import datetime


# Create your views here.

# def current_time(self):


@login_required
def todolist(request):
    if request.method == "POST":
        form = Taskform(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manager = request.user
            instance.save()
            messages.success(request, ("New task added!!"))
        else:
            messages.error(request, ("Can't add!!"))
        return redirect('todolist')
    else:
        all_task = Tasklist.objects.filter(manager=request.user)
        paginator = Paginator(all_task, 4)
        page = request.GET.get('pg')
        all_task = paginator.get_page(page)
        current = localtime()

        return render(request, 'todolist.html', {'all_task': all_task, 'current': current})


def contact(request):
    contact_form = Contactform()
    if request.method == "POST":
        contact_form = Contactform(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, ("Message sent!!"))
        else:
            messages.error(request, ("Can't send!! Check all fields!"))
        return redirect('contact')
    else:
        return render(request, 'contactform.html', {'contact_form': contact_form})


def about(request):
    context = {
        'wc_text': "Welcome to  about us"
    }
    return render(request, 'about.html', context)


def delete_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.manager == request.user:
        task.delete()
        messages.success(request, 'Task deleted!')
    else:
        messages.error(request, 'Access Restricted!! You are not allowed here!')
    return redirect('todolist')


def edit_task(request, task_id):
    if request.method == "POST":
        task_obj = Tasklist.objects.get(pk=task_id)
        form = Taskform(request.POST or None, instance=task_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Task Edited!!")
        return redirect('todolist')
    else:
        task_obj = Tasklist.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})


def done_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.manager == request.user:
        if task.done == False:
            task.done = True
        elif task.done == True:
            task.done = False
        task.save()
        messages.success(request, 'Task status updated!')
    else:
        messages.error(request, 'Access Restricted!! You are not allowed here!')
    return redirect('todolist')


def index(request):
    context = {
        'wc_text': "Welcome to  Index"
    }
    return render(request, 'index.html', context)
