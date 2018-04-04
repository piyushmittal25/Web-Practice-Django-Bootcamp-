from django.shortcuts import render

# Create your views here.
def helpy(request):
    mydic={}
    return render(request,'firstapp/helpy.html',context=mydic)
