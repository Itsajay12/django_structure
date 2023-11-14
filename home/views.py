from django.shortcuts import render

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
  return render(request,'index2.html')