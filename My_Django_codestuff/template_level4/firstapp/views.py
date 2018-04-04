from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
    contentdic={'wishstring':'Congrates','text':'hello world','date':datetime.datetime.now(),'activeinfo1':'active'}
    return render(request,'firstapp/index.html',context=contentdic)

def base(request):
    return render(request,'firstapp/base.html',context={'activeinfo2':'active'})
def other(request):
    return render(request,'firstapp/other.html',context={'activeinfo3':'active'})
