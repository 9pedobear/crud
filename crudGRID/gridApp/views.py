from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(request):
    employees = Employees.objects.all()
    context = {
        'employees' : employees
    }
    return render(request, template_name='show.html', context=context)

def addnew(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request,'index.html',{'form':form})
