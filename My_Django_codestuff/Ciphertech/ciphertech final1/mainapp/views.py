from django.shortcuts import render
from mainapp.forms import TeamInfoForm,TeamUserForm
from django.http import HttpResponseRedirect
from datetime import datetime,timedelta,timezone
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
                if teaminfoObject.start_time == None:
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

######### Question1 View
@login_required
def Question1View(request):
    team_profile=models.teaminfo.objects.get(team = request.user)
    questioninfo=models.question.objects.get(pk=1)
    resultant_string=""
    valueinbox=""
    timeup=False
    disable_part=False
    if team_profile.ques1_part1_score==0:
        part1_complete=False
    else:
        part1_complete=True

    ###
    total_time_afterstarting= datetime.now(timezone.utc) - team_profile.start_time
    if total_time_afterstarting.total_seconds() > 300:
        timeup=True
    #print(total_time_afterstarting.total_seconds())
    ###
    if not timeup:
        if request.method == 'POST':
            answer_get=request.POST.get('answer')
            if not part1_complete:
                if  questioninfo.ans_part1 == answer_get:
                    team_profile.last_submit_time = datetime.now(timezone.utc)
                    team_profile.total_time= datetime.now(timezone.utc) - team_profile.start_time
                    team_profile.ques1_part1_score = questioninfo.score_part1
                    team_profile.totalscore+=questioninfo.score_part1
                    team_profile.save()
                    part1_complete=True
                else:
                    #valueinbox = answer_get
                    resultant_string="Wrong Answer!!!"
            else:
                if  questioninfo.ans_part2 == answer_get:
                    team_profile.last_submit_time = datetime.now(timezone.utc)
                    team_profile.total_time= datetime.now(timezone.utc) - team_profile.start_time
                    team_profile.ques1_part2_score = questioninfo.score_part2
                    team_profile.totalscore+=questioninfo.score_part2
                    team_profile.save()
                    resultant_string="Right Answer!!!"
                    disable_part=True
                else:
                    #valueinbox = answer_get
                    resultant_string="Wrong Answer!!!"

        if  team_profile.ques1_part2_score!=0:
            disable_part=True
            resultant_string= "Question Completed"
    else:
        disable_part=True
        resultant_string="---------Time up-----------"
    content_dic={"result":resultant_string,'disabling':disable_part,'boxvalue':valueinbox,'part1complete':part1_complete}
    return render(request,'mainapp/questions/question1.html',context=content_dic)
##################################

########Question2
@login_required
def Question2View(request):
    team_profile=models.teaminfo.objects.get(team = request.user)
    questioninfo=models.question.objects.get(pk=2)
    resultant_string=""
    valueinbox=""
    timeup=False
    disable_part=False
    if team_profile.ques2_part1_score==0:
        part1_complete=False
    else:
        part1_complete=True

    ###
    total_time_afterstarting= datetime.now(timezone.utc) - team_profile.start_time
    if total_time_afterstarting.total_seconds() > 300:
        timeup=True
    #print(total_time_afterstarting.total_seconds())
    ###
    if not timeup:
        if request.method == 'POST':
            answer_get=request.POST.get('answer')
            if not part1_complete:
                if  questioninfo.ans_part1 == answer_get:
                    team_profile.last_submit_time = datetime.now(timezone.utc)
                    team_profile.total_time= datetime.now(timezone.utc) - team_profile.start_time
                    team_profile.ques2_part1_score = questioninfo.score_part1
                    team_profile.totalscore+=questioninfo.score_part1
                    team_profile.save()
                    part1_complete=True
                else:
                    #valueinbox = answer_get
                    resultant_string="Wrong Answer!!!"
            else:
                if  questioninfo.ans_part2 == answer_get:
                    team_profile.last_submit_time = datetime.now(timezone.utc)
                    team_profile.total_time= datetime.now(timezone.utc) - team_profile.start_time
                    team_profile.ques2_part2_score = questioninfo.score_part2
                    team_profile.totalscore+=questioninfo.score_part2
                    team_profile.save()
                    resultant_string="Right Answer!!!"
                    disable_part=True
                else:
                    #valueinbox = answer_get
                    resultant_string="Wrong Answer!!!"

        if  team_profile.ques2_part2_score!=0:
            disable_part=True
            resultant_string= "Question Completed"
    else:
        disable_part=True
        resultant_string="---------Time up-----------"
    content_dic={"result":resultant_string,'disabling':disable_part,'boxvalue':valueinbox,'part1complete':part1_complete}
    return render(request,'mainapp/questions/question2.html',context=content_dic)
##################################

###########Question3
@login_required
def Question3View(request):
    team_profile=models.teaminfo.objects.get(team = request.user)
    questioninfo=models.question.objects.get(pk=3)
    resultant_string=""
    valueinbox=""
    timeup=False
    disable_part=False
    if team_profile.ques3_part1_score==0:
        part1_complete=False
    else:
        part1_complete=True

    ###
    total_time_afterstarting= datetime.now(timezone.utc) - team_profile.start_time
    if total_time_afterstarting.total_seconds() > 300:
        timeup=True
    print(total_time_afterstarting.total_seconds())
    ###
    if not timeup:
        if request.method == 'POST':
            answer_get=request.POST.get('answer')
            if not part1_complete:
                if  questioninfo.ans_part1 == answer_get:
                    team_profile.last_submit_time = datetime.now(timezone.utc)
                    team_profile.total_time= datetime.now(timezone.utc) - team_profile.start_time
                    team_profile.ques3_part1_score = questioninfo.score_part1
                    team_profile.totalscore+=questioninfo.score_part1
                    team_profile.save()
                    part1_complete=True
                else:
                    #valueinbox = answer_get
                    resultant_string="Wrong Answer!!!"
            else:
                if  questioninfo.ans_part2 == answer_get:
                    team_profile.last_submit_time = datetime.now(timezone.utc)
                    team_profile.total_time= datetime.now(timezone.utc) - team_profile.start_time
                    team_profile.ques3_part2_score = questioninfo.score_part2
                    team_profile.totalscore+=questioninfo.score_part2
                    team_profile.save()
                    resultant_string="Right Answer!!!"
                    disable_part=True
                else:
                    #valueinbox = answer_get
                    resultant_string="Wrong Answer!!!"

        if  team_profile.ques3_part2_score!=0:
            disable_part=True
            resultant_string= "Question Completed"
    else:
        disable_part=True
        resultant_string="---------Time up-----------"
    content_dic={"result":resultant_string,'disabling':disable_part,'boxvalue':valueinbox,'part1complete':part1_complete}
    return render(request,'mainapp/questions/question3.html',context=content_dic)
##################################

###########Question4
@login_required
def Question4View(request):
    team_profile=models.teaminfo.objects.get(team = request.user)
    questioninfo=models.question.objects.get(pk=4)
    resultant_string=""
    valueinbox=""
    timeup=False
    disable_part=False
    if team_profile.ques4_part1_score==0:
        part1_complete=False
    else:
        part1_complete=True

    ###
    total_time_afterstarting= datetime.now(timezone.utc) - team_profile.start_time
    if total_time_afterstarting.total_seconds() > 300:
        timeup=True
    print(total_time_afterstarting.total_seconds())
    ###
    if not timeup:
        if request.method == 'POST':
            answer_get=request.POST.get('answer')
            if not part1_complete:
                if  questioninfo.ans_part1 == answer_get:
                    team_profile.last_submit_time = datetime.now(timezone.utc)
                    team_profile.total_time= datetime.now(timezone.utc) - team_profile.start_time
                    team_profile.ques4_part1_score = questioninfo.score_part1
                    team_profile.totalscore+=questioninfo.score_part1
                    team_profile.save()
                    part1_complete=True
                else:
                    #valueinbox = answer_get
                    resultant_string="Wrong Answer!!!"
            else:
                if  questioninfo.ans_part2 == answer_get:
                    team_profile.last_submit_time = datetime.now(timezone.utc)
                    team_profile.total_time= datetime.now(timezone.utc) - team_profile.start_time
                    team_profile.ques4_part2_score = questioninfo.score_part2
                    team_profile.totalscore+=questioninfo.score_part2
                    team_profile.save()
                    resultant_string="Right Answer!!!"
                    disable_part=True
                else:
                    #valueinbox = answer_get
                    resultant_string="Wrong Answer!!!"

        if  team_profile.ques4_part2_score!=0:
            disable_part=True
            resultant_string= "Question Completed"
    else:
        disable_part=True
        resultant_string="---------Time up-----------"
    content_dic={"result":resultant_string,'disabling':disable_part,'boxvalue':valueinbox,'part1complete':part1_complete}
    return render(request,'mainapp/questions/question4.html',context=content_dic)
##############

#########################QUESTION5
@login_required
def Question5View(request):
    team_profile=models.teaminfo.objects.get(team = request.user)
    questioninfo=models.question.objects.get(pk=5)
    resultant_string=""
    valueinbox=""
    timeup=False
    disable_part=False
    if team_profile.ques5_part1_score==0:
        part1_complete=False
    else:
        part1_complete=True

    ###
    total_time_afterstarting= datetime.now(timezone.utc) - team_profile.start_time
    if total_time_afterstarting.total_seconds() > 300:
        timeup=True
    print(total_time_afterstarting.total_seconds())
    ###
    if not timeup:
        if request.method == 'POST':
            answer_get=request.POST.get('answer')
            if not part1_complete:
                if  questioninfo.ans_part1 == answer_get:
                    team_profile.last_submit_time = datetime.now(timezone.utc)
                    team_profile.total_time= datetime.now(timezone.utc) - team_profile.start_time
                    team_profile.ques5_part1_score = questioninfo.score_part1
                    team_profile.totalscore+=questioninfo.score_part1
                    team_profile.save()
                    part1_complete=True
                else:
                    #valueinbox = answer_get
                    resultant_string="Wrong Answer!!!"
            else:
                if  questioninfo.ans_part2 == answer_get:
                    team_profile.last_submit_time = datetime.now(timezone.utc)
                    team_profile.total_time= datetime.now(timezone.utc) - team_profile.start_time
                    team_profile.ques5_part2_score = questioninfo.score_part2
                    team_profile.totalscore+=questioninfo.score_part2
                    team_profile.save()
                    resultant_string="Right Answer!!!"
                    disable_part=True
                else:
                    #valueinbox = answer_get
                    resultant_string="Wrong Answer!!!"

        if  team_profile.ques5_part2_score!=0:
            disable_part=True
            resultant_string= "Question Completed"
    else:
        disable_part=True
        resultant_string="---------Time up-----------"
    content_dic={"result":resultant_string,'disabling':disable_part,'boxvalue':valueinbox,'part1complete':part1_complete}
    return render(request,'mainapp/questions/question5.html',context=content_dic)
#######

###################Question 6
@login_required
def Question6View(request):
    team_profile=models.teaminfo.objects.get(team = request.user)
    questioninfo=models.question.objects.get(pk=6)
    resultant_string=""
    valueinbox=""
    timeup=False
    disable_part=False
    if team_profile.ques6_part1_score==0:
        part1_complete=False
    else:
        part1_complete=True

    ###
    total_time_afterstarting= datetime.now(timezone.utc) - team_profile.start_time
    if total_time_afterstarting.total_seconds() > 300:
        timeup=True
    print(total_time_afterstarting.total_seconds())
    ###
    if not timeup:
        if request.method == 'POST':
            answer_get=request.POST.get('answer')
            if not part1_complete:
                if  questioninfo.ans_part1 == answer_get:
                    team_profile.last_submit_time = datetime.now(timezone.utc)
                    team_profile.total_time= datetime.now(timezone.utc) - team_profile.start_time
                    team_profile.ques6_part1_score = questioninfo.score_part1
                    team_profile.totalscore+=questioninfo.score_part1
                    team_profile.save()
                    part1_complete=True
                else:
                    #valueinbox = answer_get
                    resultant_string="Wrong Answer!!!"
            else:
                if  questioninfo.ans_part2 == answer_get:
                    team_profile.last_submit_time = datetime.now(timezone.utc)
                    team_profile.total_time= datetime.now(timezone.utc) - team_profile.start_time
                    team_profile.ques6_part2_score = questioninfo.score_part2
                    team_profile.totalscore+=questioninfo.score_part2
                    team_profile.save()
                    resultant_string="Right Answer!!!"
                    disable_part=True
                else:
                    #valueinbox = answer_get
                    resultant_string="Wrong Answer!!!"

        if  team_profile.ques6_part2_score!=0:
            disable_part=True
            resultant_string= "Question Completed"
    else:
        disable_part=True
        resultant_string="---------Time up-----------"
    content_dic={"result":resultant_string,'disabling':disable_part,'boxvalue':valueinbox,'part1complete':part1_complete}
    return render(request,'mainapp/questions/question6.html',context=content_dic)
#############
