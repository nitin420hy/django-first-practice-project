from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Employee

def employee_info_views(request):
    employees=Employee.objects.all()
    data={'employees':employees}
    res=render(request,'testapp/employees.html',data)
    return res

def greeting(request):
    s="<h1>HELLO and Welcome to first view of testapp</h1> <p>This is Landing page</p>"
    return HttpResponse(s)
def showContact(request):
    s="<h1>Contact Page</h1>"
    s+="<p>Website: mynitin.com</p>"
    s+="<p>Mobile: 047047042</p>"
    s+="<p>Email: gvfbkhrwk@gmail.com</p>"
    return HttpResponse(s)

def about(request):
    text="This is an about page"
    return render(request,'testapp/about.html',{'text':text})
