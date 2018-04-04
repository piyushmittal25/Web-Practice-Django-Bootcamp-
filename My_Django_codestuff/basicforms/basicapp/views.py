from django.shortcuts import render
from basicapp import form
# Create your views here.
def index(request):
    return render(request,'basicapp/index.html')

def formview(request):
    formi=form.formclass()
    if request.method == 'POST':
        formi=form.formclass(request.POST)
        if formi.is_valid():
            print("Printing data of form")
            print("Name :"+formi.cleaned_data['name'])
            print("Email :"+formi.cleaned_data['email'])
            print("Text :"+formi.cleaned_data['text'])
    return render(request,'basicapp/formpage.html',context={'form':formi})
