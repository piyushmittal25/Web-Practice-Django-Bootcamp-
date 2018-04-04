from django.shortcuts import render
from django.views.generic  import (View,TemplateView,DetailView,
                                    UpdateView,DeleteView,ListView,CreateView)
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from . import models
# Create your views here.

class indexView(View):
    def get(self,request):
        return render(request,"index.html",context={'injectme':'I am from views.py file'})

class HomeView(TemplateView):
    template_name="basicapp/home.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['welcome']='Hi i am injected from views.py file'
        return context

class schoollistview(ListView):
    template_name="basicapp/schoolslist.html"
    model=models.School #this automatically generate context dictionary in which key is school_list and value is list of all school object

class schooldetailview(DetailView):
    template_name="basicapp/schooldetail.html"
    model=models.School#this automatically generate context dictionary in which key is school and value is object specified by primary key in url
    context_object_name="schooldetail" #to change  key of context dictionary accordingly

class schoolcreateview(CreateView):
    model=models.School
    fields=('name','location','principal')

class schoolupdateview(UpdateView):
    model=models.School
    fields=('name','principal')

class schooldeleteview(DeleteView):
    model=models.School
    success_url=reverse_lazy('basicapp:schoolslist')
