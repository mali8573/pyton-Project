from django.contrib.auth import login, logout, get_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from task_managment_app1.forms import TaskForm, UserForm, PersonalForm, TeamForm
from task_managment_app1.models import Task, Worker, TaskStatus, Role


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'task_managment_app1/account/login.html',{'form':form})
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Worker(user=user).save()
            login(request, user)
            return redirect('personal_details')
    else:
        form = UserCreationForm()
    return render(request, 'task_managment_app1/account/register.html', {'form': form})
@login_required(login_url='/app1/login')
def logout_view(request):
    logout(request)
    return redirect('home')
def home_view(request):
    return render(request, 'home.html')
@login_required(login_url='/app1/login')
def all_tasks_view(request):
    worker_id=request.GET.get('worker_filter')
    status_val = request.GET.get('status_filter')
    if not hasattr(request.user, 'worker'):
        return redirect('error')
    if request.user.worker.role != Role.ADMIN:
        if request.user.worker.team:
            tasks=Task.objects.filter(team=request.user.worker.team)
        else:
            tasks = Task.objects.none()
    else:
        tasks=Task.objects.all()

    if(worker_id and worker_id!="all"):
        tasks=tasks.filter(operator_id=worker_id)
    if(status_val and status_val!="all"):
        tasks=tasks.filter(status=status_val)
    context = {'tasks':tasks,
                'workers':Worker.objects.all(),
                'status_choices':TaskStatus.choices
                     }
    return render(request, 'task_managment_app1/admin/all_tasks.html',context)
@login_required(login_url='/app1/login')
def add_task_view(request):
    if not hasattr(request.user, 'worker'):
        return redirect('error')

    if request.user.worker.role != Role.ADMIN:
        return redirect('error')
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_tasks')
    else:
        form = TaskForm()
    return render(request, 'task_managment_app1/admin/add_task.html',{'form':form})


@login_required(login_url='/app1/login')
def personal_datails_view(request):
    current_user = get_object_or_404(User, pk=request.user.id)
    current_worker, created = Worker.objects.get_or_create(user=request.user)
    if request.method == "POST":
        user_form=UserForm(request.POST,instance=request.user)
        worker_form=PersonalForm(request.POST,instance=current_worker)
        if user_form.is_valid() and worker_form.is_valid():
            user_form.save()
            worker_form.save()
            return redirect('home')
    else:
        user_form=UserForm(instance=current_user)
        worker_form=PersonalForm(instance=current_worker)
    context = {'user_form':user_form, 'worker_form':worker_form}
    return render(request, 'task_managment_app1/account/personal_details.html',context)
@login_required(login_url='/app1/login')
def add_team_view(request):
    if not hasattr(request.user, 'worker'):
        return redirect('error')

    if request.user.worker.role != Role.ADMIN:
        return redirect('error')
    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_tasks')
    else:
        form = TeamForm()
    return render(request, 'task_managment_app1/admin/add_team.html',{'form':form})
@login_required(login_url='/app1/login')
def update_task_view(request,taskid):
    if not hasattr(request.user, 'worker'):
        return redirect('error')

    if request.user.worker.role != Role.ADMIN:
        return redirect('error')
    task=get_object_or_404(Task, pk=taskid)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('all_tasks')

    else:
        if task.status != TaskStatus.NEW:
            return redirect('error')
        form = TaskForm(instance=task)
    return render(request, 'task_managment_app1/admin/add_task.html',{'form':form})
@login_required(login_url='/app1/login')
def delete_task_view(request,taskid):
    if not hasattr(request.user, 'worker'):
        return redirect('error')

    if request.user.worker.role != Role.ADMIN:
        return redirect('error')
    task=get_object_or_404(Task, pk=taskid)
    if request.method == "POST":
        if task.status!=TaskStatus.NEW:
            return redirect('error')
        else:
            task.delete()
        return redirect('all_tasks')
    if task.status != TaskStatus.NEW:
        return redirect('error')
    return render(request, 'task_managment_app1/admin/delete_task.html',{'task':task})
@login_required(login_url='/app1/login')
def update_status_task_view(request,taskid):
    if not hasattr(request.user, 'worker'):
        return redirect('error')
    task=get_object_or_404(Task, pk=taskid)
    if task.status==TaskStatus.NEW:
        if task.team == request.user.worker.team:
            task.status=TaskStatus.ACTIVE
            task.operator=request.user.worker
            task.save()

    elif task.status==TaskStatus.ACTIVE:
        if task.operator==request.user.worker:
            task.status=TaskStatus.FINISHED
            task.save()
    return redirect('all_tasks')


def error_view(request):
    return render(request, 'task_managment_app1/admin/error.html')

