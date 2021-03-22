from django.conf.urls import url
from django.urls import include
from testapp import views

urlpatterns = [
    url('^$',views.greeting),
    url('contact/',views.showContact),
    url('about/',views.about),
]
