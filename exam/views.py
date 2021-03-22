from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def showTest(request):
    s="<p>This is Show Test Page</p>"
    return HttpResponse(s)

def showResult(request):
    s="<p>This is show result page</p>"
    return HttpResponse(s)
