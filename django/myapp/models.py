from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name
    
class task(models.Model):
    tittle = models.CharField(max_length=200)
    description = models.TextField
    project = models.ForeignKey(Project, on_delete=models.CASCADE )
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.tittle + ' - ' + self.project.name
    
    '''on_delete sirve para decirle que hacer 
    cuando el proyecto sea eliminado y todas sus tareas
    correspondientes esten en la otra tabla'''
    '''CASCADE sirve para eliminar la herencia correspondiente
    de los proyectos eliminados en forma de cascada'''
    
