from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home1(request):
  return render(request,'index.html')
def home2(request):
  return HttpResponse("page 2")
