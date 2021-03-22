from django.conf.urls import url
from django.urls import include
from exam import views

urlpatterns = [
    url('test/',views.showTest),
    url('result/',views.showResult),
]
