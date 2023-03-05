from django.shortcuts import render, redirect , get_list_or_404, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, task
from .forms import CreateNewTask, CreateNewProjects

# Create your views here.


def index(request):
    title = 'Django course'
    return render(request, 'index.html', {'title': title})


def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello Wordl %s</h1>" % username)


def about(request):
    user = 'Tavo'
    return render(request, 'about.html', {'username': user})


def Projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html',
                  {'projects': projects}
                  )


def Tasks(request,):
    # Task = task.objects.get()
    tasks = task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })


def create_task(request):
  # if request.method == 'GET':
     #show interface
    return render(request, 'tasks/create_tasks.html', {
        'form': CreateNewTask()
    })
   #else:
       #task.objects.create(title=request.POST["title"], description=request.POST["description"],
                         #  projects_id=2)
      # return redirect('/Tasks/')

 #else:
      #  task.objects.create(title=request.POST["title"],
       # description=request.POST["description"], project_id=2)
           # return redirect('/Tasks/')
        
def create_projects(request):
    if request.method == 'GET':
        return render(request, 'projects/create_projects.html', {
            'form': CreateNewProjects()
        })
    else:
        Project.objects.create(name=request.POST["name"])
        return redirect('projects')
    
def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
   # project = Project.objects.get(id=id)
    #print(Project)
    tasks = task.objects.filter(project_id=id)
    return render(request,'projects/detail.html',{
        'project':project,
        'task': tasks
    })