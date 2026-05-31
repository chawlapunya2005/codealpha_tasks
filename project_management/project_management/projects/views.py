from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Project, Task, Comment

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'home.html')

@login_required
def dashboard(request):
    owned = Project.objects.filter(owner=request.user)
    member = Project.objects.filter(members=request.user)
    my_tasks = Task.objects.filter(assigned_to=request.user).exclude(status='done')[:5]
    return render(request, 'projects/dashboard.html', {
        'owned_projects': owned,
        'member_projects': member,
        'my_tasks': my_tasks,
    })

@login_required
def create_project(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        color = request.POST.get('color', '#e8c547')
        project = Project.objects.create(owner=request.user, name=name, description=description, color=color)
        messages.success(request, f'Project "{name}" created!')
        return redirect('project_detail', pk=project.pk)
    return render(request, 'projects/create_project.html')

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.user != project.owner and request.user not in project.members.all():
        messages.error(request, "You don't have access to this project.")
        return redirect('dashboard')
    todo_tasks = project.tasks.filter(status='todo')
    inprogress_tasks = project.tasks.filter(status='inprogress')
    done_tasks = project.tasks.filter(status='done')
    all_users = User.objects.exclude(pk=project.owner.pk)
    return render(request, 'projects/project_detail.html', {
        'project': project,
        'todo_tasks': todo_tasks,
        'inprogress_tasks': inprogress_tasks,
        'done_tasks': done_tasks,
        'all_users': all_users,
    })

@login_required
def create_task(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        priority = request.POST.get('priority', 'medium')
        due_date = request.POST.get('due_date') or None
        assigned_id = request.POST.get('assigned_to')
        assigned_to = User.objects.get(pk=assigned_id) if assigned_id else None
        Task.objects.create(
            project=project, title=title, description=description,
            priority=priority, due_date=due_date,
            assigned_to=assigned_to, created_by=request.user
        )
        messages.success(request, 'Task created!')
    return redirect('project_detail', pk=project_pk)

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(task=task, author=request.user, content=content)
    comments = task.comments.all().order_by('created')
    members = list(task.project.members.all()) + [task.project.owner]
    return render(request, 'projects/task_detail.html', {'task': task, 'comments': comments, 'members': members})

@login_required
def update_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.status = request.POST.get('status', task.status)
        task.save()
    return redirect('project_detail', pk=task.project.pk)

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    project_pk = task.project.pk
    task.delete()
    messages.success(request, 'Task deleted.')
    return redirect('project_detail', pk=project_pk)

@login_required
def add_member(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    if request.user == project.owner and request.method == 'POST':
        user_id = request.POST.get('user_id')
        try:
            user = User.objects.get(pk=user_id)
            project.members.add(user)
            messages.success(request, f'{user.username} added to project!')
        except User.DoesNotExist:
            pass
    return redirect('project_detail', pk=project_pk)

@login_required
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    project.delete()
    messages.success(request, 'Project deleted.')
    return redirect('dashboard')
