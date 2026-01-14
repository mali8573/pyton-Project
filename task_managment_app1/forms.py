

from django import forms
from django.contrib.auth.models import User

from task_managment_app1.models import Task, Worker, Team

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'targetDate','team']
        widgets = {
            "name":forms.TextInput(attrs={'class':'form-control'}),
            "description":forms.Textarea(attrs={'class':'form-control'}),
            "targetDate":forms.DateInput(attrs={'class':'form-control','type':'date'}),
            "team":forms.Select(attrs={'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        # קבלת המשתמש מה-View
        user = kwargs.pop('user', None)
        super(TaskForm, self).__init__(*args, **kwargs)

        if user and hasattr(user, 'worker'):
            if user.worker.role == 'ADMIN':
                self.fields['team'].widget = forms.HiddenInput()
                self.fields['team'].required = False
                # if 'operator' in self.fields:
                #     self.fields['operator'].queryset = Worker.objects.filter(team=current_worker.team)
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

