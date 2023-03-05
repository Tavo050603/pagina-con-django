from django import forms
class CreateNewTask(forms.Form):
    title = forms.CharField(label="Tutulo de tarea", max_length=200, widget=forms.TextInput(attrs={'class':'input'}))
    description = forms.CharField(label="Descripcion de la tarea" ,widget=forms.Textarea(attrs={'class':'input'}))
    
class CreateNewProjects(forms.Form):
    name = forms.CharField(label='Nombre del projecto', max_length=200,  widget=forms.TextInput(attrs={'class':'input'}))