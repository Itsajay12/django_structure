from django.shortcuts import render
from .models import*
from home.forms import*

# Create your views here.
from django.http import HttpResponse

def home1(request):
  dic={
    "name":"Ajay",
    "Age":20
    }
  return render(request,'index.html',dic)
# def home2(request):
#   return HttpResponse("page 2")
def home2(request):
  query=student.objects.all()
  return render(request,'index2.html',{'query':query})

def employee(request):
  query=Employee.objects.all()
  return render(request,'employee.html',{'query':query})


def from1(request):
  form=StudentForm()
  if(request.method=='POST'):
    form=StudentForm(request.POST)
    if form.is_valid():
      form.save()
      return home2(request)
  return render(request,'form.html',{'form':form})
  
def form2(request):
 form=EmployeeForm()
 if(request.method=='POST'):
   form=EmployeeForm(request.POST)
   if form.is_valid():
     form.save()
     return employee(request)
 return render(request,'from2.html',{'form':form})