from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<strong>Hurray!!</strong>")

# Create your views here.