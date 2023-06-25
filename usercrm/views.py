from django.shortcuts import render,redirect
from crm.forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
def userregister(request):
    form=CreateUserForm()
    if request.method=='POST':
        formobj = CreateUserForm(request.POST)
        if formobj.is_valid():
            formobj.save()
            return redirect('addstudenturl')
        else:
            messages.error(request,formobj.errors)
    return render(request,'admin/userregister.html',{'form':form})