

from django import forms
from django.contrib.auth.models import User

from task_managment_app1.models import Task, Worker, Team


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'targetDate','team']
        widgets = {
            "title":forms.TextInput(attrs={'class':'form-control'}),
            "description":forms.Textarea(attrs={'class':'form-control'}),
            "targetDate":forms.DateInput(attrs={'class':'form-control','type':'date'}),
            "team":forms.Select(attrs={'class':'form-control'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']
        widgets = {
            "first_name":forms.TextInput(attrs={'class':'form-control'}),
            "last_name":forms.TextInput(attrs={'class':'form-control'}),
            "email":forms.EmailInput(attrs={'class':'form-control'}),
        }



class PersonalForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = [ 'phone', 'address','role', 'team']
        widgets = {
            "phone":forms.TextInput(attrs={'class':'form-control'}),
            "address":forms.Textarea(attrs={'class':'form-control'}),
            "role": forms.Select(attrs={'class': 'form-control'}),
            "team":forms.Select(attrs={'class':'form-control'}),
        }
class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = [ 'name' ]
        widgets = {
            "name":forms.TextInput(attrs={'class':'form-control'})
        }

