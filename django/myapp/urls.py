from django.urls import path
from . import views

urlpatterns = [
        path('', views.index,name="index"),
        path('About/', views.about,name="About"),
        path('hello/<str:username>', views.hello,name="hello"),
        path('Tasks/', views.Tasks,name="tasks"),
        path('Projects/', views.Projects,name="projects"),
        path('Projects/<int:id>', views.project_detail,name="project_detail"),
        path('Create task/',views.create_task,name="create_tasks"),
        path('Create Projects/', views.create_projects,name="create_projects"),
        
]
