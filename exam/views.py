from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def showTest(request):
    que="Who developed C Language?"
    a="Ken Thompson"
    b="Dennis Ritchie"
    c="Bjarne Stroustrup"
    d="Saurabh Shukla"
    level="Level defined"
    data={'que':a,'a':a,'b':b,'c':c,'d':d,'level':level}
    res=render(request,'exam/test.html',context=data)
    return res

def showResult(request):
    s="<p>This is show result page</p>"
    return HttpResponse(s)
