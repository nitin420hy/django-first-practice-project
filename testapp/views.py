from django.shortcuts import render
from django.http import HttpResponse
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
    msg='this is an about page'
    l1=[10,20,30]
    x=30
    return render(request,'testapp/about.html',{'x':x,'msg':msg,'l1':l1})
