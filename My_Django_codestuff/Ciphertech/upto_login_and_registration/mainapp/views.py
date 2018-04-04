from django.shortcuts import render
from mainapp.forms import TeamInfoForm,TeamUserForm
from django.http import HttpResponseRedirect
from datetime import datetime
from mainapp.models import teaminfo
from mainapp import models
# Create your views here.
######
from django.contrib.auth import authenticate,login,logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
#####
def startpage(request):
    return render(request,'mainapp/startpage.html')

def SignUpView(request):
    if request.method=='POST':
        TeamLoginInfoForm=TeamUserForm(data=request.POST)
        TeamDetailInfoForm=TeamInfoForm(data=request.POST)
        if TeamLoginInfoForm.is_valid() and TeamDetailInfoForm.is_valid():
            TeamLoginInfo=TeamLoginInfoForm.save()
            TeamLoginInfo.set_password(TeamLoginInfo.password)
            TeamLogin=TeamLoginInfoForm.save()
            TeamDetail=TeamDetailInfoForm.save(commit=False)
            TeamDetail.team=TeamLogin
            TeamDetailInfoForm.save()
            return HttpResponseRedirect('ciphertech/')
        else:
            content_dic={'error1':TeamLoginInfo.errors,'error2':TeamDetailInfo.errors}
            return render(request,'mainapp/signup.html',context=content_dic)
    else:
        TeamLoginInfoForm=TeamUserForm()
        TeamDetailInfoForm=TeamInfoForm()
        content_dic={'TeamForm':TeamLoginInfoForm,"TeamDetail":TeamDetailInfoForm}
        return render(request,'mainapp/signup.html',context=content_dic)

def LeaderboardView(request):
    teamslist=list(teaminfo.objects.all())
    teamslist.sort(key= lambda x:(-x.totalscore,x.total_time))
    content_dic={'teamlist':teamslist,'rank':1}
    return render(request,'mainapp/leaderboard.html',context=content_dic)

def InstructionView(request):
    return render(request,'mainapp/instruction.html')

def LogInView(request):
    if request.method == "POST":
        teamname=request.POST.get('teamname')
        password=request.POST.get('password')
        team=authenticate(username=teamname,password=password)
        if team:
            if team.is_active:
                login(request,team)
                teaminfoObject=models.teaminfo.objects.get(team = team)
                teaminfoObject.start_time=datetime.now()
                teaminfoObject.save()
                return render(request,'mainapp/questionslist.html')
            else:
                content_dic={'error':'You are a Inactive User Contact Admin'}
                return render(request,'mainapp/login.html',context=content_dic)
        else:
            content_dic={'error':'Invalid TeamName or Password'}
            return render(request,'mainapp/login.html',context=content_dic)
    else:
        return render(request,'mainapp/login.html')

def QuestionListView(request):
    return render(request,'mainapp/questionslist.html')

#####Question View

# @login_required
# def Question1View(request):
#     if request.method == 'POST':

######
