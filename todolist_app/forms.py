from django import forms
from todolist_app.models import Tasklist, Contact
from django.forms.widgets import DateTimeInput


class Taskform(forms.ModelForm):
    class Meta:
        model = Tasklist
        fields = ['task', 'done', 'task_deadline']
        widgets = {
            'task_deadline': forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'class': 'datetimefield'}),
        }


class Contactform(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
