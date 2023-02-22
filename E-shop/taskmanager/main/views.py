from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.http import HttpResponseRedirect
from .forms import ResumeForm

def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def mybasket(request):
    return render(request, 'main/my basket.html')


def newproduct(request):
    error = ''
    if request.method  == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неправильной'

    form = TaskForm()
    context = {
            'form': form,
            'error': error
    }
    return render(request, 'main/new product.html', context)

def upload_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = ResumeForm
    return render(request, 'files/resume.html', {'form':form})
