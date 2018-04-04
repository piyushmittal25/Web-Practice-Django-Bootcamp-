from django import forms
from django.contrib.auth.models import User
from mainapp.models import teaminfo

class TeamUserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model=User
        labels={'username':'Team Name','password':'Password'}
        fields=('username','email','password')

class TeamInfoForm(forms.ModelForm):
    class Meta():
        model=teaminfo
        fields=('member1','member2','collegename')
        labels={
                'member1':'Member1 Name',
                'member2':'Member2 Name',
                'collegename':'College Name',
                }
