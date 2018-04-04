from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    dic={'insert_here':'La La La are dewanon mujhe ....'}
    return render(request,'first_app/index.html',context=dic)
# Create your views here.
