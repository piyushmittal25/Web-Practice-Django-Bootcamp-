from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<strong>I am just need help!!<strong>")
