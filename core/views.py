from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Sum

from .forms import CustomUserCreationForm, TaskForm


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('user_login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'auth/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('project_list')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'auth/login.html')

@login_required
def project_list(request):
    projects = Project.objects.filter(assigned_to=request.user)
    return render(request, 'projects/project_list.html', {'projects': projects})


@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, assigned_to=request.user)
    tasks = project.tasks.all()

    # Handle form submission
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.project = project
            new_task.save()
            return redirect('project_detail', pk=pk)
    else:
        form = TaskForm()

    return render(request, 'projects/project_detail.html', {'project': project, 'tasks': tasks, 'form': form})


@login_required
def accept_project(request, pk):
    project = get_object_or_404(Project, pk=pk, assigned_to=request.user)
    if project.status == 'Pending':
        project.status = 'Accepted'
        project.save()
        return redirect('project_list')
    return redirect('project_detail', pk=pk)

@login_required
def update_task_status(request, task_id):
    task = get_object_or_404(Task, pk=task_id, project__assigned_to=request.user)
    project = task.project

    if task.status == 'Pending':
        task.status = 'Completed'
        task.save()

        # Check if all tasks in the project are completed
        if project.tasks.filter(status='Pending').count() == 0:
            project.status = 'Completed'
            project.save()

    return redirect('project_detail', pk=task.project.id)


@login_required
def project_progress(request, pk):
    project = get_object_or_404(Project, pk=pk, assigned_to=request.user)
    tasks = project.tasks.all()
    
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(status='Completed').count()
    progress = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0

    total_score = tasks.aggregate(total_score=Sum('score'))['total_score'] or 0
    score_obtained = tasks.filter(status='Completed').aggregate(obtained_score=Sum('score'))['obtained_score'] or 0

    return render(request, 'projects/project_progress.html', {
        'project': project,
        'tasks': tasks,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'progress': progress,
        'total_score': total_score,
        'score_obtained': score_obtained,  # Pass score_obtained to template
    })
