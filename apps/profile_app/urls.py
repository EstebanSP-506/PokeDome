from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^$', views.get_trainer),
    url(r'^(?P<trainer_ID>\d+)$', views.profile),
    url(r'^(?P<trainer_ID>\d+)/remove$', views.remove),
]
