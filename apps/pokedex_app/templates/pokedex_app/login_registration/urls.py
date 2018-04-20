from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^$', views.index),
    url(r'^logout$', views.logout),
    url(r'^main$', views.main),
    url(r'^main/register$', views.register),
    url(r'^main/login$', views.login),
]
