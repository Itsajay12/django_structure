from django.shortcuts import render
from .forms import*
# Create your views here.
def index(request):
    return render(request,'index.html')
# def add_data(request):
    # if request.method=='POST':
    #     print("1")
    #     form=EmployeeForm(request.POST)
    #     print(form)
    #     if form.is_valid():
    #         print(2)
    #         form.save()
    #     else:
    #         print("not valid")
    #         return index(request)
    # return render(request,'form.html')
def add_data(request):
    if request.method=='POST':
        emp_id=request.POST['emp_id']
        emp_name=request.POST['emp_name']
        emp_email=request.POST['emp_email']
        emp_address=request.POST['emp_address']
        query=Employee.objects.create(emp_id=emp_id,emp_name=emp_name,emp_email=emp_email,emp_address=emp_address)
        
        query.save()
        return index(request)
    return render(request,'form.html')