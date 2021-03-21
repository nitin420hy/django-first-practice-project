from django.shortcuts import render
from django.http import HttpResponse
def greeting(request):
    s="<h1>HELLO !!! </h1>"
    return HttpResponse(s)
