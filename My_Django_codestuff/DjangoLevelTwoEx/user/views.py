from django.shortcuts import render
from django.http import HttpResponseRedirect
from user.models import userinfo
from user import forms
# Create your views here.

def index(request):
    return render(request,'user_app/index.html')

def users(request):
    userslist=userinfo.objects.order_by('First_name')
    contentdic={'UserInfo':userslist}
    return render(request,'user_app/userinfo.html',contentdic)

def newuser(request):
    newform=forms.userform()
    if request.method=='POST':
        newform=forms.userform(request.POST)
        if newform.is_valid():
            newform.save()
        #return HttpResponseRedirect('/user/newuser/thanksyou')  #this make to return to homepage
        return thankyou(request)
    return render(request,'user_app/newuser.html',context={'userform':newform})

def thankyou(request):
    return render(request,'user_app/thankyou.html')
