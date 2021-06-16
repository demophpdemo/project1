from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

# Add and Show Data
def index(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            form = UserForm()
    else:
        form = UserForm()
        
    stu = User.objects.all().order_by('id')
    context = {'form':form,'stu':stu}
    template_name = "app/crud/add.html"
    return render(request,template_name,context)

# Update
def update(request,id):
    pi = User.objects.get(pk=id)
    if request.method == "POST":
    
        form = UserForm(request.POST,instance=pi)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Error')
    else:
        
        form = UserForm(instance=pi)
        return render(request,'app/crud/update.html',{'form':form})

# Delete Data
def delete(request,id):
    
    if request.method == "POST":
        info = User.objects.get(id=id)
        info.delete()
        return HttpResponseRedirect('/')

