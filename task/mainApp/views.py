from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    return render(request, 'mainApp/index.html', {'title': 'Страница', 'tasks': tasks})


def about(request):
    return render(request, 'mainApp/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма неверна'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'mainApp/make.html', context)